import pandas as pd
import os

# 保存フォルダ
folder_path = "samplecode/excel_merge"
os.makedirs(folder_path, exist_ok=True)

# サンプルデータ
data_list = [
    {"月": [1, 1, 1], "売上": [10000, 15000, 12000], "利益": [2000, 3000, 2500]},
    {"月": [2, 2, 2], "売上": [18000, 21000, 19000], "利益": [3500, 4200, 3900]},
    {"月": [3, 3, 3], "売上": [25000, 27000, 26000], "利益": [5000, 5200, 5100]},
]

# ファイル名
file_names = ["sales_2024_01.xlsx", "sales_2024_02.xlsx", "sales_2024_03.xlsx"]

# Excel出力
for data, name in zip(data_list, file_names):
    df = pd.DataFrame(data)
    df.to_excel(os.path.join(folder_path, name), index=False)

print("✅ サンプルExcelを3つ作成しました！")
