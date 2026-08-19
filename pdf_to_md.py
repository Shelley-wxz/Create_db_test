
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MinerU 批量 PDF 转 Markdown 脚本
功能：扫描 rsc/ 和 springer/ 目录下的 PDF 文件，通过 MinerU 精准解析 API 转换为 Markdown 文件，
      输出到 rsc-spr-mds/ 目录，文件名规则与之前的 LlamaParse 脚本一致。

使用方法：
  1. 将本脚本放在与 rsc/、springer/ 目录同级的位置
  2. 修改下方的 MINERU_API_TOKEN 为你的 MinerU API Token
  3. 运行: python mineru_pdf_to_md.py
"""

import os
import time
import zipfile
import requests
from pathlib import Path
from typing import List, Tuple, Optional

# ============================================================
# 配置区域 - 请修改此处
# ============================================================

# MinerU API Token（在 MinerU API 管理页面创建）
MINERU_API_TOKEN = "sk-hkBZF58RQoYwt8B6S8W4Shs2oFCEleJEEyPYldBTdtYSxtSi"

# API 基础地址
MINERU_API_BASE = "https://mineru.net"

# 模型版本：pipeline / vlm（推荐）
MODEL_VERSION = "vlm"

# 语言：en 表示英文文档
LANGUAGE = "en"

# 源目录
DIR_PATHS = ["springer", "rsc"]

# 输出目录
OUTPUT_DIR = "rsc-spr-mds"

# 批量上传每批最大文件数（API 限制 50）
BATCH_SIZE = 50

# 轮询间隔（秒）
POLL_INTERVAL = 5

# 最大轮询次数（防止无限等待）
MAX_POLL_COUNT = 120

def get_pdf_files(dir_paths: List[str]) -> List[Tuple[str, str]]:
    """获取所有目录下的 PDF 文件列表，返回 (目录路径, 文件名) 元组"""
    all_files = []
    for mypath in dir_paths:
        if os.path.exists(mypath):
            files = [
                f for f in os.listdir(mypath)
                if os.path.isfile(os.path.join(mypath, f)) and f.endswith(".pdf")
            ]
            all_files.extend([(mypath, f) for f in files])
        else:
            print(f"警告: 目录 {mypath} 不存在，已跳过。")
    return all_files

def get_output_filename(scientific_paper: str) -> str:
    """
    根据文件名生成输出文件名
    - 包含 "article"：例如 123-article456.pdf -> parsed_output-456.pdf.md
    - 不包含 "article"：例如 123-456.pdf -> parsed_output-123-456.pdf.md
    """
    if "article" in scientific_paper:
        article_part = scientific_paper.split("article")[-1]
        return f"parsed_output-{article_part}.md"
    else:
        return f"parsed_output-{scientific_paper}.md"

def upload_batch(
    token: str,
    file_paths: List[str],
    file_names: List[str],
    model_version: str,
    language: str,
) -> Optional[str]:
    """
    批量申请上传链接，上传文件，返回 batch_id。
    失败返回 None。
    """
    url = f"{MINERU_API_BASE}/api/v4/file-urls/batch"
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    data = {
        "files": [{"name": name} for name in file_names],
        "model_version": model_version,
        "language": language,
    }

    try:
        resp = requests.post(url, headers=header, json=data, timeout=30)
        resp.raise_for_status()
        result = resp.json()
        if result.get("code") != 0:
            print(f"  申请上传链接失败: {result.get('msg')}")
            return None

        batch_id = result["data"]["batch_id"]
        upload_urls = result["data"]["file_urls"]

        # 上传文件
        for i, file_path in enumerate(file_paths):
            if i >= len(upload_urls):
                break
            upload_url = upload_urls[i]
            with open(file_path, "rb") as f:
                put_resp = requests.put(upload_url, data=f, timeout=120)
                if put_resp.status_code == 200:
                    print(f"  上传成功: {os.path.basename(file_path)}")
                else:
                    print(f"  上传失败: {os.path.basename(file_path)}, HTTP {put_resp.status_code}")

        return batch_id

    except Exception as e:
        print(f"  批量上传异常: {e}")
        return None

def poll_batch_results(
    token: str,
    batch_id: str,
) -> List[dict]:
    """轮询批量任务结果，返回结果列表"""
    url = f"{MINERU_API_BASE}/api/v4/extract-results/batch/{batch_id}"
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    for attempt in range(MAX_POLL_COUNT):
        try:
            resp = requests.get(url, headers=header, timeout=30)
            resp.raise_for_status()
            result = resp.json()
            if result.get("code") != 0:
                print(f"  查询失败: {result.get('msg')}")
                return []

            results = result.get("data", {}).get("extract_result", [])
            all_done = all(r.get("state") == "done" for r in results)
            any_failed = any(r.get("state") == "failed" for r in results)

            if all_done:
                return results
            elif any_failed:
                # 返回结果（包含失败的）
                return results
            else:
                # 打印进度
                statuses = [r.get("state", "") for r in results]
                file_names = [r.get("file_name", "") for r in results]
                progress_info = [
                    f"{fn}: {st}" for fn, st in zip(file_names, statuses)
                ]
                print(f"  等待中... (第{attempt + 1}次轮询) {progress_info}")
                time.sleep(POLL_INTERVAL)

        except Exception as e:
            print(f"  轮询异常: {e}")
            time.sleep(POLL_INTERVAL)

    print("  轮询超时，部分文件可能尚未完成解析")
    return []

def download_and_extract(zip_url: str, output_path: str) -> bool:
    """下载 zip 包并提取 full.md"""
    try:
        resp = requests.get(zip_url, timeout=120)
        resp.raise_for_status()
        zip_data = resp.content

        # 从内存中解压
        with zipfile.ZipFile(__import__("io").BytesIO(zip_data)) as zf:
            # 查找 full.md
            md_files = [n for n in zf.namelist() if n.endswith("full.md")]
            if md_files:
                md_content = zf.read(md_files[0]).decode("utf-8")
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(md_content)
                return True
            else:
                print(f"  zip 中未找到 full.md，文件列表: {zf.namelist()}")
                return False
    except Exception as e:
        print(f"  下载/解压失败: {e}")
        return False

if __name__ == "__main__":
    # 1. 检查 Token
    if MINERU_API_TOKEN == "YOUR_MINERU_API_TOKEN_HERE":
        print("错误: 请先修改脚本中的 MINERU_API_TOKEN 为你的 MinerU API Token")
        exit(1)

    # 2. 确保输出目录存在
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 3. 获取所有 PDF 文件
    all_files = get_pdf_files(DIR_PATHS)
    if not all_files:
        print("未找到任何 PDF 文件，请检查 rsc/ 和 springer/ 目录。")
        exit(0)

    print(f"共找到 {len(all_files)} 个 PDF 文件，开始处理...")
    print(f"输出目录: {OUTPUT_DIR}")
    print(f"模型版本: {MODEL_VERSION}")
    print("-" * 60)

    # 4. 分批处理
    success_count = 0
    fail_count = 0

    for batch_start in range(0, len(all_files), BATCH_SIZE):
        batch = all_files[batch_start : batch_start + BATCH_SIZE]
        print(f"\n处理第 {batch_start // BATCH_SIZE + 1} 批 ({len(batch)} 个文件)...")

        # 准备文件路径和名称
        file_paths = [os.path.join(mypath, fname) for mypath, fname in batch]
        file_names = [fname for _, fname in batch]

        # 上传
        batch_id = upload_batch(MINERU_API_TOKEN, file_paths, file_names, MODEL_VERSION, LANGUAGE)
        if batch_id is None:
            print("  该批上传失败，跳过。")
            for _, fname in batch:
                fail_count += 1
            continue

        # 轮询结果
        results = poll_batch_results(MINERU_API_TOKEN, batch_id)

        # 处理结果
        for res in results:
            file_name = res.get("file_name", "")
            state = res.get("state", "")
            zip_url = res.get("full_zip_url", "")
            err_msg = res.get("err_msg", "")

            output_filename = get_output_filename(file_name)
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            if state == "done" and zip_url:
                if download_and_extract(zip_url, output_path):
                    print(f"  已保存: {output_path}")
                    success_count += 1
                else:
                    print(f"  解压失败: {file_name}")
                    fail_count += 1
            else:
                print(f"  解析失败: {file_name} - {err_msg}")
                fail_count += 1

        # 批次间稍作等待，避免限频
        time.sleep(1)

    # 5. 汇总
    print("\n" + "=" * 60)
    print(f"处理完成! 成功: {success_count}, 失败: {fail_count}, 总计: {len(all_files)}")
