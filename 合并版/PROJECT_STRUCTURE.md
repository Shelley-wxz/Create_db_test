all/
├── main.py                # [核心] 总控脚本，负责按顺序调度各模块
├── database_HEA.csv       # [输入] 论文元数据表
├── README.md              # 项目说明文档
├── requirements.txt       # 项目依赖包
├── downloaders/           # [下载模块] 存放文献下载脚本
│   ├── download_rsc.py
│   ├── download_elsevier.py
│   └── download_springer.py
├── processors/            # [处理模块] 存放解析、转换与合并脚本
│   ├── xml_extractor2.py
│   └── pdf_to_md.py
└── final/                # [配置模块] 存放提示词与辅助配置
    ├── ds_mult_prompts.py
    ├── merge_metadata_and_results.py
    ├── comprehensive_dict2csv.py
    └── prompts.py