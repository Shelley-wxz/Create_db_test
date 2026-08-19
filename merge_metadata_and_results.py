import json
import csv
from json import JSONDecodeError
import pandas as pd

def _build_detail(details_dict):
    """从 dict 中提取 method 和 parameters，构建详情字符串。"""
    if not details_dict:
        return 'N/A'
    method = details_dict.get('method', '') or ''
    parameters = details_dict.get('parameters', {}) or {}
    detail_parts = [method] if method else []
    if isinstance(parameters, dict):
        for k, v in parameters.items():
            param_str = f"{k.replace('_', ' ').capitalize()}: {v}"
            detail_parts.append(param_str)
    else:
        if parameters:
            detail_parts.append(str(parameters))
    return ', '.join(detail_parts) if detail_parts else 'N/A'


def cd_to_csv(papers_names: list, papers_jsons: list) -> None:
    """
    Args:
        papers_jsons: list of responses from LLM (each response contains a ```json block)
    Returns:
        Writes data to db_HEAs.csv
    """
    with open('db_HEAs.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        headers = [
            'id', 'Paper', "Name", 'Alloy', 'Nb of phase', 'Phase',
            'Experimental or theoretical', 'Experimental details',
            'Theoretical details', 'Special conditions', 'Type of solution'
        ]
        writer.writerow(headers)

        for i, json_data in enumerate(papers_jsons):
            # Extract JSON block from response
            try:
                json_data = json_data.split("```json")[1].split("```")[0]
            except IndexError:
                print("No valid ```json block found in this paper's response")
                continue

            # Load JSON data into a Python dictionary
            try:
                data = json.loads(json_data)
            except JSONDecodeError as e:
                print(f"json decode error for paper {papers_names[i]}: {e}")
                continue

            # Iterate over each alloy in the data
            for alloy_key, alloy_data in data.items():
                # Basic info
                id = i
                paper = papers_names[i]
                name = papers_names[i]

                alloy = alloy_data.get('chemical_formula', alloy_key)

                # Extract phases
                crystallographic_phases = alloy_data.get('crystallographic_phases', [])

                if len(crystallographic_phases) == 0:
                    crystallographic_phases = alloy_data.get('phases', [])

                nb_of_phase = len(crystallographic_phases)
                if nb_of_phase == 0:
                    print(f"No crystallographic phases found for {alloy}")
                    print(alloy_data)

                phases = []
                for phase in crystallographic_phases:
                    structure = phase.get('structure', '')
                    structure_lower = structure.lower()
                    if structure_lower == 'body-centered cubic':
                        structure_abbrev = 'BCC'
                    elif structure_lower == 'face-centered cubic':
                        structure_abbrev = 'FCC'
                    elif structure_lower == 'hexagonal':
                        structure_abbrev = 'HCP'
                    else:
                        # If the structure isn't one of the known ones, just use it directly
                        structure_abbrev = structure if structure else 'Unknown'

                    # If it's explicitly intermetallic
                    if phase.get('phase_type', '').lower() == 'intermetallic':
                        structure_abbrev += ' (Intermetallic)'

                    phases.append(structure_abbrev)

                phase_str = ' + '.join(phases) if phases else 'N/A'

                # Determine if it's experimental, theoretical, or both
                exp_or_theo = 'N/A'
                experimental_details = 'N/A'
                theoretical_details = 'N/A'

                # Check for synthesis_or_calculation
                synthesis = alloy_data.get('synthesis_or_calculation', None)
                if synthesis:
                    raw_type = synthesis.get('type', 'N/A')
                    # 统一小写比较，修复大小写不匹配问题
                    exp_or_theo_lower = raw_type.lower() if raw_type else 'n/a'
                    exp_or_theo = raw_type if raw_type else 'N/A'

                    is_exp = exp_or_theo_lower in ['experimental', 'theoretical and experimental', 'combination', 'both']
                    is_theo = exp_or_theo_lower in ['theoretical', 'theoretical and experimental', 'combination', 'both']

                    if is_exp:
                        # 从 synthesis 自身的 method + parameters 构建 experimental details
                        experimental_details = _build_detail({
                            'method': synthesis.get('method', ''),
                            'parameters': synthesis.get('parameters', {})
                        })
                        # 如果是 combination/both 类型，且 synthesis 内部有 experimental 子键，优先使用
                        if exp_or_theo_lower in ['combination', 'both', 'theoretical and experimental']:
                            exp_sub = synthesis.get('experimental', {})
                            if exp_sub:
                                experimental_details = _build_detail(exp_sub)

                    if is_theo:
                        # 从 synthesis 自身的 method + parameters 构建 theoretical details
                        theoretical_details = _build_detail({
                            'method': synthesis.get('method', ''),
                            'parameters': synthesis.get('parameters', {})
                        })
                        # 如果是 combination/both 类型，且 synthesis 内部有 theoretical 子键，优先使用
                        if exp_or_theo_lower in ['combination', 'both', 'theoretical and experimental']:
                            theo_sub = synthesis.get('theoretical', {})
                            if theo_sub:
                                theoretical_details = _build_detail(theo_sub)
                        # 也检查 alloy 级别的 theoretical_details（作为补充）
                        theo_alloy = alloy_data.get('theoretical_details', {})
                        if theo_alloy and theoretical_details == 'N/A':
                            theoretical_details = _build_detail(theo_alloy)

                    # combination / both / theoretical and experimental: 两个列都有相同数据
                    if exp_or_theo_lower in ['combination', 'both', 'theoretical and experimental']:
                        combined = experimental_details
                        if theoretical_details != 'N/A' and theoretical_details != experimental_details:
                            combined = f"{experimental_details}; {theoretical_details}"
                        experimental_details = combined
                        theoretical_details = combined
                else:
                    # 没有 synthesis_or_calculation，检查 synthesis_details
                    syn_details = alloy_data.get('synthesis_details', {})
                    if syn_details:
                        method = syn_details.get('method', '')
                        if method:
                            exp_or_theo = 'Experimental'
                        experimental_details = _build_detail(syn_details)

                special_conditions = alloy_data.get('special_conditions', 'N/A')
                type_of_solution = alloy_data.get('phase_classification', 'N/A')

                row = [
                    id, paper, name, alloy, nb_of_phase, phase_str,
                    exp_or_theo, experimental_details,
                    theoretical_details, special_conditions, type_of_solution
                ]
                writer.writerow(row)

        print("Data has been successfully written to 'db_HEAs.csv'")

if __name__ == "__main__":
    df = pd.read_csv('database_of_all_prompts.csv')

    # batches = [
    #     "result_multiple_prompts-batch-mds-rsc.csv",
    #     "result_multiple_prompts-batch-mds-rsc2.csv",
    #     "result_multiple_prompts-batch-mds-springer.csv",
    #     "result_multiple_prompts-batch-mds-springer2.csv",
    # ]
    # for batch in batches:
    #     temp = pd.read_csv(f'{batch}')
    #     df = pd.concat([df, temp], ignore_index=True)

    # for i in range(2, 11):
    #     temp = pd.read_csv(f'result_multiple_prompts-batch-mds-1127-{i}.csv')
    #     df = pd.concat([df, temp], ignore_index=True)

    df = df.loc[df["context_missread_bug"] == True].reset_index(drop=True)
    # 修复：链式替换，每一步基于上一步的结果
    df['reference'] = (df['article']
        .str.replace('.txt', '')
        .str.replace('parsed_output--', '')
        .str.replace('parsed_output-', '')
        .str.replace('.pdf.md', '')
        .str.replace('10.1039-', '')
    )

    metadata = pd.read_csv("database_HEA.csv")
    # metadata = metadata.loc[metadata["source"] == "ELSVIER"].drop(columns=["Unnamed: 0", "Unnamed: 0.1"])

    metadata = metadata.groupby(['reference','source','URL']).first().reset_index()
    metadata["reference"] = metadata["reference"].str.replace('10.1039-', '') #rsc

    metadata.drop_duplicates(inplace=True)

    merged_df = pd.merge(df, metadata, on='reference', how='left')

    papers_names = (merged_df['article']
        .str.replace('10.1039-', ''))

    merged_df['article'] = merged_df['article'].str.replace('10.1039-', '', regex=False)
    merged_df['pdf_url'] = merged_df['pdf_url'].str.replace('10.1039-', '', regex=False)

    merged_df.to_csv("database_of_raw_responses.csv")

    # Process the files and print the titles
    cd_to_csv(papers_names=list(papers_names), papers_jsons=list(merged_df["prompt5"]))