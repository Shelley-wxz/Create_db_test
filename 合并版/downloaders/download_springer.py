import requests
import pandas as pd
import os

if __name__ == "__main__":
    df = pd.read_csv('database_HEA.csv')

    springer_papers = df.loc[df["source"]=="springer"].drop_duplicates(subset=['URL'])
    
    os.makedirs("springer", exist_ok=True)
    
    for idx, row in springer_papers.iterrows():
        link = row["URL"]
        doi = row["Doi"]
        
        # 构建PDF下载URL: article/ -> content/pdf/
        request_url = link.replace("article/", "content/pdf/") + ".pdf"
        
        # 文件名使用DOI
        doi_filename = doi.replace("https://doi.org/", "").replace("/", "-") + ".pdf"
        save_path = "springer/" + doi_filename
        
        print(f"Downloading: {doi_filename}")
        response = requests.get(request_url, timeout=60)
        
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"Article downloaded successfully: {save_path}")
        else:
            print(f"Failed to download article. Status code: {response.status_code}")
