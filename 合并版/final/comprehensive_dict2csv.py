import json
import re
import csv
from json import JSONDecodeError
import pandas as pd
from json_repair import repair_json


def extract_phase_from_details(structure: str, details: str, phase_type: str) -> str:
    """
    Extract phase information from structure and details fields.
    """
    base_structure = structure
    structure_lower = structure.lower()
    structure_mapping = {
        'body-centered cubic': 'BCC',
        'face-centered cubic': 'FCC',
        'body-centered tetragonal': 'BCT',
        'hexagonal': 'HCP'
    }
    
    for key, value in structure_mapping.items():
        if key in structure_lower:
            base_structure = value
            break
    
    if not details:
        return base_structure
    
    details = details.lower()
    phase_str = base_structure
    
    special_phases = {
        'a2': 'A2',
        'b2': 'B2',
        'b19': 'B19',
        'l12': 'L12',
        'c14': 'C14',
        'c15': 'C15',
        'cr2ta': 'Cr2Ta',
        'ti2ni': 'Ti2Ni',
        'spinel': 'Spinel',
        'o-phase': 'O-phase',
        'laves': 'Laves',
        'dr+id': 'DR+ID',
        'amorphous': 'Amorphous'
    }
    
    for key, value in special_phases.items():
        if (key in details.lower()) and (key not in structure_lower) and (key not in phase_str.lower()):
            if phase_str == base_structure:
                phase_str += (" "+value) 
            else:
                if key in ["a2", "b2", "l12", "c14", "c15", "laves"]:
                    phase_str += " "+value
                else:
                    phase_str += f" + {value}"
    
    oxide_patterns = [
        r'cro\d+',
        r'al2o3',
        r'(co-fe)7w6',
        r'alni'
    ]
    
    for pattern in oxide_patterns:
        matches = re.findall(pattern, details.lower())
        for match in matches:
            compound = match.upper()
            if 'CRO' in compound:
                compound = f"CrO{compound[-1]}"
            elif 'AL2O3' in compound:
                compound = 'Al2O3'
            elif '(CO-FE)7W6' in compound:
                compound = '(Co-Fe)7W6'
            elif 'ALNI' in compound:
                compound = 'AlNi'
            phase_str += f" + {compound}"
    
    if 'martensite' in details.lower():
        phase_str += ' martensite'
    
    if 'tivzr' in details.lower() and 'taw' in details.lower():
        phase_str += ' (TiVZr + TaW)'
    
    if phase_type.lower() == 'intermetallic' and 'laves' not in phase_str.lower():
        phase_str += ' (Intermetallic)'
    
    return phase_str


def _build_detail(method, parameters) -> str:
    """
    Build a detail string from method and parameters dict.
    Returns 'N/A' if both are empty/None.
    """
    if not method and not parameters:
        return 'N/A'
    
    detail_parts = []
    if method:
        detail_parts.append(f"Method: {method}")
    if isinstance(parameters, dict):
        for k, v in parameters.items():
            param_str = f"{k.replace('_', ' ').capitalize()}: {v}"
            detail_parts.append(param_str)
    elif parameters:
        detail_parts.append(str(parameters))
    
    return ', '.join(detail_parts) if detail_parts else 'N/A'


def cd_to_csv(output_file: str, papers_names: list, names_list: list,  papers_jsons: list) -> None:
    """
    Args:
        output_file: name of the output file
        papers_names: list of paper names
        names_list: list of authors names
        papers_jsons: list of responses from LLM (each response contains a ```json block)
    Returns:
        Writes data to output2.csv
    """
    with open(output_file, 'w', newline='',encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        headers = [
            'id', 'Paper', 'Name', 'Alloy', 'Nb of phase', 'Phase',
            'Experimental or theoretical', 'Experimental details',
            'Theoretical details', 'Special conditions', 'Type of solution'
        ]
        writer.writerow(headers)

        for i, json_data in enumerate(papers_jsons):
            # Extract JSON block from response
            try:
                if '```json' not in json_data:
                    json_data = json_data.split("```python")[1].split("```")[0]
                else:
                    json_data = json_data.split("```json")[1].split("```")[0]
            except (TypeError, IndexError, AttributeError) as e:
                print(f"No valid ```json block found in this paper's response {e}")
                print(json_data)
                continue

            # Load JSON data into a Python dictionary
            try:
                data = json.loads(json_data)
            except JSONDecodeError as e:
                print(f"json decode error for paper {papers_names[i]}: {e}")
                try:
                    repaired = repair_json(json_data)
                    data = json.loads(repaired)
                    print(f"  -> 已通过 json_repair 修复，继续处理")
                except Exception as repair_err:
                    print(f"  -> json_repair 也无法修复: {repair_err}")
                    # 打印出错行附近内容
                    ...
                    skipped.append(papers_names[i])
                    continue

            # Iterate over each alloy in the data
            for alloy_key, alloy_data in data.items():
                # Basic info
                no_solid_solution = False
                id = i
                paper = papers_names[i]
                name = names_list[i]
                alloy = alloy_data.get('chemical_formula', alloy_key)

                # Extract phases
                crystallographic_phases = alloy_data.get('crystallographic_phases', [])

                if len(crystallographic_phases) == 0:
                    crystallographic_phases = alloy_data.get('phases', [])

                
                phases = []
                for phase in crystallographic_phases:
                    phase_str = extract_phase_from_details(
                        phase.get('structure', ''),
                        phase.get('details', ''),
                        phase.get('phase_type', '')
                    )
                    if (phase_str) and (phase_str not in " ".join(phases)):
                        phases.append(phase_str)


                # Join phases and remove duplicates
                phase_str = ' + '.join(sorted(set(phases))) if phases else 'N/A'

                lower_phase_str = phase_str.lower().replace("-","")
                precipitates = alloy_data.get('precipitates', [])
                if len(precipitates) > 0:
                    for precipitate in precipitates:
                        if (type(precipitate) == str):
                            if (precipitate.lower() not in lower_phase_str):
                                phase_str += " + " + precipitate
                        elif precipitate.get("chemical_formula", "N/A").lower() not in lower_phase_str:
                            phase_str += " + " + precipitate.get("chemical_formula", "N/A")
                        else:
                            continue
                        
                    
                nb_of_phase = phase_str.count("+") + 1

                for structure in ["BCC", "FCC", "HCP"]:
                    if structure in phase_str:
                        no_solid_solution = False
                        break
                    no_solid_solution = True


                if "morphous" in phase_str and no_solid_solution:
                    type_of_solution = "Amorphous"
                elif no_solid_solution:
                    type_of_solution = "Intermetallic"
                else:
                    type_of_solution = alloy_data.get('phase_classification', 'N/A')

                # === Determine if it's experimental, theoretical, or both ===
                exp_or_theo = 'N/A'
                experimental_details = 'N/A'
                theoretical_details = 'N/A'

                synthesis = alloy_data.get('synthesis_or_calculation', None)
                if synthesis:
                    raw_type = synthesis.get('type', 'N/A')
                    exp_or_theo = raw_type if raw_type else 'N/A'
                    exp_or_theo_lower = exp_or_theo.lower()
                    
                    # Build detail string from synthesis level method+parameters
                    synth_method = synthesis.get('method') or ''
                    synth_params = synthesis.get('parameters') or {}
                    synth_detail = _build_detail(synth_method, synth_params)
                    
                    if exp_or_theo_lower == 'experimental':
                        # Experimental: experimental details has data, theoretical is N/A
                        experimental_details = synth_detail
                        theoretical_details = 'N/A'
                        
                    elif exp_or_theo_lower == 'theoretical':
                        # Theoretical: theoretical details has data, experimental is N/A
                        experimental_details = 'N/A'
                        theoretical_details = synth_detail
                        
                    elif exp_or_theo_lower in ['both', 'combination', 'theoretical and experimental']:
                        # Combination/both: both columns have the same data
                        # For "both" type, also try reading from nested experimental/theoretical keys
                        if synth_detail != 'N/A':
                            combined_detail = synth_detail
                        else:
                            # Try nested experimental key
                            exp_sub = synthesis.get('experimental', {})
                            if exp_sub:
                                exp_method = exp_sub.get('method') or ''
                                exp_params = exp_sub.get('parameters') or {}
                                combined_detail = _build_detail(exp_method, exp_params)
                            else:
                                combined_detail = synth_detail
                        
                        experimental_details = combined_detail
                        theoretical_details = combined_detail
                else:
                    # No synthesis_or_calculation, try synthesis_details
                    syn_details = alloy_data.get('synthesis_details', {})
                    method = syn_details.get('method', '')
                    parameters = syn_details.get('parameters', {})
                    detail = _build_detail(method, parameters)
                    if detail != 'N/A':
                        experimental_details = detail

                special_conditions = alloy_data.get('special_conditions', 'N/A')

                row = [
                    id, paper, name, alloy, nb_of_phase, phase_str,
                    exp_or_theo, experimental_details,
                    theoretical_details, special_conditions, type_of_solution
                ]
                writer.writerow(row)

        print(f"Data has been successfully written to '{output_file}'")


if __name__ == "__main__":
    df = pd.read_csv('database_of_raw_responses.csv')
    cd_to_csv(
        output_file="final_db_HEAs.csv",
        papers_names=list(df["pdf_url"]),
        names_list=list(df["article"]),
        papers_jsons=list(df["prompt5"]),
    )