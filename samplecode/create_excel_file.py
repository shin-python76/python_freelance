# create_excel_file.py
# PythonでExcelファイルを新規作成して保存するサンプル
# ライブラリ：openpyxl

from openpyxl import Workbook

# 新しいExcelブックを作成
wb = Workbook()

# アクティブなシートを取得
sheet = wb.active

# シート名を変更
sheet.title = "テストシート"

# A1セルに文字を書き込み
sheet["A1"] = "こんにちは！Pythonから書き込みました。"

# Excelファイルを保存
wb.save("sample_created.xlsx")

print("✅ Excelファイルを作成しました！")
