import os
import csv
from phenotype_engine import PhenotypeExtractor

def run_agent_pipeline(input_folder, output_csv):
    extractor = PhenotypeExtractor(reference_real_width_mm=50.0)
    results = []
    
    valid_extensions = ('.ply', '.pcd', '.xyz')
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(valid_extensions)]
    
    print(f"Agent 已启动: 发现 {len(files)} 个待处理样本。")
    
    for file_name in files:
        file_path = os.path.join(input_folder, file_name)
        print(f"正在分析: {file_name} ...")
        
        data_row = extractor.process_point_cloud(file_path)
        results.append(data_row)
        
    # 严格保持原始文件名与数据精度
    fieldnames = ["Original_Filename", "Plant_Height_mm", "Leaf_Area_mm2", "Status"]
    
    with open(output_csv, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
            
    print(f"批处理完成。结果已保存至: {output_csv}")

if __name__ == "__main__":
    INPUT_DIR = "./data"
    OUTPUT_FILE = "high_throughput_phenotypes_GWAS_input.csv"
    run_agent_pipeline(INPUT_DIR, OUTPUT_FILE)