# HEA Paper Processing Pipeline

高熵合金（High Entropy Alloy）论文数据处理全流程编排工具。

## 概述

本管道自动化处理来自三个学术出版商（RSC、Springer、Elsevier）的高熵合金学术论文，包括：
- 论文全文下载
- PDF/XML 转换为可分析文本
- 基于 LLM 的结构化信息抽取（晶体结构、相组成、合成方法等）
- 元数据合并与最终 CSV 生成

## 管道流程

```
Phase 1 (并行下载)                          Phase 2 (并行处理)                        Phase 3 (串行处理)
┌─────────────┐                              ┌──────────────┐                         ┌─────────────────────────┐
│ Step 1      │                              │ Step 4       │                         │ Step 6                    │
│ download_   │                              │ pdf_to_md.py │                         │ ds_mult_prompts.py        │
│ rsc.py      │                              │              │                         │ (LLM多轮分析)             │
│ RSC PDF下载  │                              │ RSC/Springer  │────────────────────────▶│ 输出: database_of_all_    │
│             │                              │ PDF转Markdown │   elsevier_txt/*.txt  │    prompts.csv            │
└─────────────┘                              └──────────────┘                         └──────────┬────────────────┘
┌─────────────┐                              ┌──────────────┐                                    │
│ Step 2      │                              │              │                         ┌────────▼────────────────┐
│ download_   │                              │ Step 5       │                         │ Step 7                  │
│ springer.py │                              │ xml_extract  │                         │ merge_metadata_and_   │
│ Springer    │                              │ 2.py         │                         │    results.py           │
│ PDF下载     │                              │ Elsevier XML │                         │ 输出: database_of_raw_  │
│             │                              │ 文本提取      │                         │    responses.csv        │
└─────────────┘                              └──────────────┘                         │         + db_HEAs.csv     │
┌─────────────┐                              └──────────────┘                         └──────────┬────────────────┘
│ Step 3      │                                   │                                             │
│ download_   │                                   ▼                                             ▼
│ elsevier.py │                            ┌──────────────────┐                     ┌─────────────────────────┐
│ Elsevier    │                            │ Step 8           │                     │ Step 9                    │
│ XML下载     │                            │ comprehensive_   │                     │ comprehensive_dict2csv.py │
│             │                            │ dict2csv.py      │                     │ 输出: final_db_HEAs.csv   │
└─────────────┘                            │ 最终CSV生成       │                     │ (最终输出)                │
                                           └──────────────────┘                     └─────────────────────────┘
```

### 步骤详解

| 步骤 | 脚本路径 | 说明 | 输入 | 输出 | 依赖 |
|------|----------|------|------|------|------|
| 1 | downloaders/download_rsc.py | 下载 RSC 来源的 PDF | database_HEA.csv (source=rsc) | rsc/*.pdf | 无 |
| 2 | downloaders/download_springer.py | 下载 Springer 来源的 PDF | database_HEA.csv (source=springer) | springer/*.pdf | 无 |
| 3 | downloaders/download_elsevier.py | 下载 Elsevier 来源的 XML | database_HEA.csv (source=elsevier) | elsevier/*.xml | 无 |
| 4 | processors/pdf_to_md.py | 将 RSC/Springer 的 PDF 转为 Markdown | rsc/ + springer/ | rsc-spr-mds/*.md | 步骤 1, 2 |
| 5 | processors/xml_extractor2.py | 从 Elsevier XML 中提取文本 | elsevier/ | elsevier_txt/*.txt | 步骤 3 |
| 6 | final/ds_mult_prompts.py | 通过 LLM 对论文进行多轮结构化分析 | elsevier_txt/ + rsc-spr-mds/ | database_of_all_prompts.csv | 步骤 4, 5 |
| 7 | final/merge_metadata_and_results.py | 合并元数据与 LLM 分析结果 | database_of_all_prompts.csv | database_of_raw_responses.csv + db_HEAs.csv | 步骤 6 |
| 8 | final/comprehensive_dict2csv.py | 生成最终综合 CSV | database_of_raw_responses.csv | final_db_HEAs.csv | 步骤 7 |

## 目录结构

### 执行前（项目文件）

```
pipeline_root/
├── database_HEA.csv          # 论文元数据表（必需）
├── main.py                   # 管道编排脚本
├── README.md                 # 本文件
├── downloaders/              # 下载模块
│   ├── download_rsc.py
│   ├── download_springer.py
│   └── download_elsevier.py
├── processors/               # 处理模块
│   ├── pdf_to_md.py
│   └── xml_extractor2.py
└── final/                    # 最终处理模块
    ├── ds_mult_prompts.py
    ├── merge_metadata_and_results.py
    ├── comprehensive_dict2csv.py
    └── prompts.py
```

### 执行后（自动生成）

```
pipeline_root/
├── rsc/                      # RSC 下载的 PDF
├── springer/                 # Springer 下载的 PDF
├── elsevier/                 # Elsevier 下载的 XML
├── rsc-spr-mds/              # RSC/Springer 的 Markdown 文件
├── elsevier_txt/             # Elsevier 提取的文本文件
├── database_of_all_prompts.csv
├── database_of_raw_responses.csv
├── db_HEAs.csv
├── final_db_HEAs.csv         # 最终输出
├── pipeline.log              # 运行日志
└── .pipeline_status.json     # 管道状态（用于断点续跑）
```

## 前置要求

### Python 包

```bash
pip install requests pandas openpyxl lxml PyPDF2 
pip install pymupdf          # xml_extractor2.py 需要（用于 PDF 格式 fallback）
```

### API 密钥（需在环境变量中设置）

| 密钥 | 用途 | 对应步骤 |
|------|------|---------|
| LLAMA_PARSE_API | LlamaParse PDF 解析 | Step 4 |
| DEEPSEEK_API_KEY 或脚本内嵌密钥 | DeepSeek LLM 分析 | Step 6 |
| X-ELS-APIKey (Elsevier API Key) | Elsevier API 访问 | Step 3 |

> 注意：部分脚本（如 download_elsevier.py、ds_mult_prompts.py）中已内嵌 API 密钥。如需更换，请直接编辑对应脚本中的密钥变量。

### database_HEA.csv 格式

该文件是管道的输入数据源，至少包含以下列：

| 列名 | 说明 |
|------|------|
| source | 来源标识：rsc / springer / elsevier（区分大小写） |
| Doi | DOI 标识符（可含 https://doi.org/ 前缀） |
| URL | Springer 来源的论文 URL |
| reference | 论文引用标识（RSC 来源用） |

## 使用方法

### 运行完整管道

```bash
python main.py
```

### 仅运行指定步骤

```bash
# 仅运行步骤 1-3（下载阶段）
python main.py --step 1,2,3

# 仅运行步骤 4（PDF 转 Markdown）
python main.py --step 4

# 仅运行步骤 6（LLM 分析）
python main.py --step 6
```

### 断点续跑

如果管道中途失败，修复问题后可以使用 --resume 从上次完成的位置继续：

```bash
python main.py --resume
```

### 强制重跑已完成步骤

```bash
python main.py --force --step 4
```

### 查看管道状态

```bash
python main.py --status
```

### 清理所有生成文件

```bash
python main.py --cleanup
```

## 故障排查

### 下载失败

- 检查网络连接
- RSC：确认 DOI 格式正确，期刊代码可自动提取
- Springer：确认 URL 可访问
- Elsevier：确认 API Key 有效，论文是否为 OA 或有权访问

### LLM 分析超时/失败

- Step 6 可能需要较长时间（取决于论文数量和长度）
- 检查 DeepSeek API 密钥是否有效
- 查看 pipeline.log 获取详细错误信息
- 可使用 --step 6 单独重跑该步骤

### PDF 解析失败

- 确认 LLAMA_PARSE_API 环境变量已设置
- 单页 PDF 会被跳过（pdf_to_md.py 的逻辑）
- 检查 rsc-spr-mds/ 目录确认解析结果

### 常见问题

| 问题 | 解决方案 |
|------|---------|
| ModuleNotFoundError | 检查是否安装了所有依赖包 |
| 403 Forbidden | 检查 API Key 和论文访问权限 |
| 输出 CSV 为空 | 检查 database_HEA.csv 的 source 列值是否匹配 |
| LLM 返回空结果 | 检查论文文本是否完整提取（查看 .md/.txt 文件） |

## 注意事项

1. **模块化结构**：项目采用模块化设计，脚本按功能分放在 `downloaders/`、`processors/`、`final/` 三个子目录中，请勿随意更改文件夹名称或脚本文件名。
2. **运行目录**：所有脚本均在 main.py 所在目录执行，确保 database_HEA.csv 放在项目根目录下。
3. **断点续跑**：.pipeline_status.json 记录已完成步骤，--resume 会跳过这些步骤。
4. **日志**：所有运行日志保存在 pipeline.log 中。
5. **清理**：--cleanup 会删除所有生成的数据和目录，但保留脚本和输入文件。
6. **Step 6 耗时**：LLM 分析步骤可能非常耗时（每篇论文 5 轮对话），建议分批处理。
