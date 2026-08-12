
import csv
import os
import time
import requests
import re

# ================= 配置区域 =================
CSV_FILE = 'database_HEA.csv'    # 您的 CSV 文件路径
OUTPUT_DIR = 'rsc'   # 下载文件保存的文件夹
DELAY = 2                       # 每次下载后的休眠时间（秒），防止触发反爬
# ===========================================

def download_rsc_pdfs():
    # 1. 创建下载目录
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 2. 设置请求头（伪装浏览器，防止 403 Forbidden）
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    # 3. 读取 CSV 文件并逐行处理
    with open(CSV_FILE, 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # 判断 source 是否为 rsc（忽略大小写）
            source = row.get('source', '').strip().lower()
            if source != 'rsc':
                continue  # 如果不是 RSC，直接跳过当前循环，进入下一行

            doi_raw = row.get('Doi', '').strip()
            title = row.get('reference')

            # 去掉 DOI 中的 URL 前缀，只保留纯 DOI
            # 例如 "https://doi.org/10.1039/D6DD00105J" -> "10.1039/D6DD00105J"
            doi = re.sub(r'^https?://doi\.org/', '', doi_raw)
            
            # 从 DOI 中自动提取期刊代码
            # RSC DOI 格式: 10.1039/XY[JournalCode][Sequence]
            # 例如 10.1039/D6DD00105J -> D=年代, 6=年份, DD=期刊代码
            # 正则: 跳过年代字母和年份数字，捕获后面两个字母
            match = re.match(r'10\.1039/[a-zA-Z]\d([a-zA-Z]{2})', doi)
            if not match:
                print(f"[跳过] 无法从 DOI 中识别期刊代码: {doi}")
                continue
                
            journal_code = match.group(1).lower()  # 提取并转为小写（如 'dd', 'ra'）

            # 拼接 PDF 下载链接
            pdf_url = f"https://pubs.rsc.org/{journal_code}/articlepdf/{doi}"
                
            path = os.path.join(OUTPUT_DIR, f"{title}.pdf")
            
            try:
                print(f"正在下载: ({doi})...")
                response = requests.get(pdf_url, headers=headers, stream=True, timeout=30)
                response.raise_for_status()
                
                # 防假文件检查：确保下载的是 PDF 而不是 HTML 报错页
                content_type = response.headers.get('Content-Type', '')
                if 'application/pdf' not in content_type:
                    print(f"[警告] {doi} 返回的不是 PDF 文件，可能是权限不足或链接错误。")
                    continue
                
                # 实际写入文件到磁盘
                with open(path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        f.write(chunk)
                        
                print(f"[成功] 已保存: {path}")
                
            except requests.exceptions.RequestException as e:
                print(f"[失败] 下载 {doi} 时出错: {e}")
            
            # 礼貌爬取：休眠几秒
            time.sleep(DELAY)

if __name__ == '__main__':
    download_rsc_pdfs()