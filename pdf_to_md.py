from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
from os import listdir
from os.path import isfile, join
import os
from PyPDF2 import PdfReader
from typing import Union
from pathlib import Path

def is_multi_page_pdf(pdf_path: Union[str, Path]) -> bool:
    """
    Check if a PDF file contains more than one page.
    """
    try:
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"No file found at {pdf_path}")
        if pdf_path.suffix.lower() != '.pdf':
            raise ValueError(f"File {pdf_path} is not a PDF")
        with open(pdf_path, 'rb') as file:
            pdf = PdfReader(file)
            return len(pdf.pages) > 1
    except Exception as e:
        print(f"Error checking PDF {pdf_path}: {str(e)}")
        return False

if __name__ == "__main__":
    # 修改：同时处理 springer 和 rsc 两个目录
    dir_paths = [
        "springer",  # Springer 的 PDF 文件目录
        "rsc"        # RSC 的 PDF 文件目录
    ]
    output_dir = "rsc-spr-mds"
    
    # 1. 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 2. 初始化 LlamaParse
    # 请确保环境变量 LLAMA_PARSE_API 已设置，或者直接在这里填入你的 API Key
    LLAMA_PARSE_API = "llx-UMMFzjEqdiXLOriBKv6pePjJbqAXoRgE9MegMTDNloojbZxY"
    parser = LlamaParse(
        api_key=LLAMA_PARSE_API,
        result_type="markdown",
        verbose=True,
        language="en"
    )
    file_extractor = {".pdf": parser}
    
    # 3. 获取所有目录下的文件列表
    all_files = []  # 存储 (目录路径, 文件名) 元组
    for mypath in dir_paths:
        if os.path.exists(mypath):
            files = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".pdf")]
            all_files.extend([(mypath, f) for f in files])
        else:
            print(f"警告: 目录 {mypath} 不存在，已跳过。")
    
    print(f"Found {len(all_files)} PDF files in total. Starting parsing...")
    
    # 4. 遍历并解析
    for mypath, scientific_paper in all_files:
        pdf_path = join(mypath, scientific_paper)
        
        # 简单的页数检查（可选，LlamaParse 也能处理单页，但保留原逻辑）
        if is_multi_page_pdf(pdf_path):
            print(f"Processing ({mypath}): {scientific_paper}...")
            try:
                documents = SimpleDirectoryReader(
                    input_files=[pdf_path],
                    file_extractor=file_extractor,
                ).load_data()
                
                # 5. 保存 Markdown
                # --- 修改开始 ---
                # 根据文件名是否包含 "article" 来应用不同的命名规则
                if "article" in scientific_paper:
                    # 规则1: 包含 "article"，提取其后的部分
                    # 例如：123-article456.pdf -> 456.pdf
                    article_part = scientific_paper.split("article")[-1]
                    output_filename = f"parsed_output-{article_part}.md"
                else:
                    # 规则2: 不包含 "article"，在文件名后追加 .md
                    # 例如：123-456.pdf -> parsed_output-123-456.pdf.md
                    output_filename = f"parsed_output-{scientific_paper}.md"
                # --- 修改结束 ---
                
                output_path = join(output_dir, output_filename)
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    for doc in documents:
                        f.write(doc.text + '\n')
                print(f"Successfully saved to {output_path}")
            except Exception as e:
                print(f"Failed to parse {scientific_paper}: {str(e)}")
        else:
            print(f"Skipping (single page or invalid): {scientific_paper}")
