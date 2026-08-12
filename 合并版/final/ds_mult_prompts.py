
import csv
import time
import os
import pandas as pd
from openai import OpenAI
from prompts import multiple_prompts

from os import listdir
from os.path import isfile, join


model = "deepseek-chat"

client = OpenAI(
    api_key="sk-be731fee2a8b43c19aad4f037a7c1f29",
    base_url="https://api.deepseek.com",
)

def walk_through_papers(scientific_papers: list, filename: str):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["article", "pdf_url", "prompt1", "prompt2", "prompt3", "prompt4", "prompt5", "context_missread_bug"])
        count = 0
        rows = []
        dir_paths = [
            "elsevier_txt",  # Elsevier 的 txt 文件目录
            "rsc-spr-mds"    # RSC 和 Springer 的 md 文件目录
        ]
        scientific_papers = []
        for mypath in dir_paths:
            if os.path.exists(mypath):
                files = [f for f in os.listdir(mypath) if f.endswith(('.txt', '.md'))]
                scientific_papers.extend([(mypath, f) for f in files])
                print(f"目录 {mypath} 中找到 {len(files)} 个文件")
            else:
                print(f"警告: 目录 {mypath} 不存在，已跳过。")
        print(f"总共待处理文件数: {len(scientific_papers)}")
        flag = False
        for current_dir, scientific_paper in scientific_papers:
            with open(join(current_dir, scientific_paper), 'r', encoding="utf-8") as f:
                try:
                    d = f.read()
                except Exception as e:
                    print(e)
                    continue
                # print(d)
            messages = [
                {"role": "system", "content": 
                        """
You are a materials science expert specializing in crystallography and high entropy alloys. Analyze scientific papers with these core behaviors:

- Process information sequentially while maintaining context between questions
- Extract and verify all quantitative data, especially chemical formulas and processing parameters
- Use proper chemical notation and consistent formatting
- Present information in structured lists
- State explicitly any uncertainties or missing information
- Pay an extra attention to the markdown tables 

For each question:
- Consider the entire paper before answering
- Cross-reference information across sections
- Flag any contradictions or inconsistencies
- Maintain scientific rigor and precision
- Present answers in clear, organized format

Quality standard: Be thorough and precise while maintaining clarity. If information is ambiguous or missing, state this explicitly.
                        """},
                {"role": "user", "content": f"Here is the paper in the markdown for your analysis: {d}"}

            ]
            responses = []
            try:
                for index, prompt in enumerate(multiple_prompts):
                    if len(responses) > 0:
                        messages.append({"role": "assistant", "content": responses[-1]})

                    messages.append({"role": "user", "content": prompt})
                    print(index)
                    # if index == 4:

                    response, finish_reason = run(messages)

                    print(response)


                    responses.append(response)

                    def check_if_finished(finish_reason):
                        print(f"finish reason: {finish_reason}")
                        if finish_reason == "length":
                            messages.append(
                                {"role": "assistant", "content": responses[-1]+"\n continue right where you dropped with the next character"}
                            )
 
                            response, finish_reason = run(messages=messages)
                            responses[index] = responses[index]+response
                            check_if_finished(finish_reason)

                    check_if_finished(finish_reason)
                    # else:
                    #     responses.append("skip")
                if len(responses[-1]) < 60:
                    responses.append(False)
                else:
                    responses.append(True)
            except Exception as e:
                print(e)
                time.sleep(100)
                continue
            rows.append([scientific_paper, scientific_paper] + responses)
            csvwriter.writerows(rows)
            rows = []



def run(messages):
    llm_request = client.chat.completions.create(
        messages=messages,
        model=model,
        stream=True,
    )
    response = ""
    for chunk in llm_request:
        ch = chunk.choices[0].delta.content
        fr = chunk.choices[0].finish_reason
        if ch:
            response += ch
            print(ch, end="")

    return response, fr


if __name__ == "__main__":
    walk_through_papers([], 'database_of_all_prompts.csv')