import os
import csv
import time
import requests
from urllib.parse import quote

# ================= 配置区域 =================
CSV_FILE = 'database_HEA.csv'
OUTPUT_DIR = 'elsevier'
API_KEY = 'a65237d2ac8fc56fdd9c91c0ae946fcf'  # 你的 API Key
DELAY = 2
# ===========================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_full_text(doi):
    """通过 Elsevier API 获取全文 XML"""
    url = f"https://api.elsevier.com/content/article/doi/{quote(doi)}"
    headers = {
        'X-ELS-APIKey': API_KEY,
        'Accept': 'text/xml',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        
        if resp.status_code == 200:
            return resp.text
        elif resp.status_code == 403:
            print(f"[403] 权限访问 {doi} 时被拒绝。")
            return None
        else:
            # 其他错误（如 404 找不到，429 限流等）静默处理或简单返回 None
            return None
    except requests.RequestException:
        return None


def main():
    if not os.path.exists(CSV_FILE):
        print(f"错误: 找不到文件 {CSV_FILE}")
        return

    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('source', '').strip().lower() != 'elsevier':
                continue
            
            doi = row.get('Doi', '').strip()
            if not doi: 
                continue
                
            # 清洗 DOI，确保只保留后缀
            if doi.startswith('http'):
                doi = doi.split('doi.org/')[-1]

            try:
                xml_content = get_full_text(doi)
                
                if xml_content:
                    safe_name = doi.replace('/', '-') + '.xml'
                    save_path = os.path.join(OUTPUT_DIR, safe_name)
                    with open(save_path, 'w', encoding='utf-8') as wf:
                        wf.write(xml_content)
                else:
                    # 仅在失败时打印提示，避免刷屏
                    print(f"[跳过] {doi} (无权限或非OA)")
                    
            except Exception as e:
                print(f"[异常] {doi}: {str(e)}")
            
            time.sleep(DELAY)

if __name__ == '__main__':
    main()