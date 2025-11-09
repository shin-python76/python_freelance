import pandas as pd
import os
import glob

# ライブラリ	主な役割	今回の使い方
# pandas	データを表形式で扱う（表計算ライブラリ）	各Excelを読み込み・結合・出力
# os	ファイルやフォルダ操作	フォルダパスを作る（os.path.join()）
# glob	ファイル検索を自動化	「sales_*.xlsx」という条件で一括取得

# フォルダパスを指定
folder_path = "samplecode/excel_merge"

# folder_path はフォルダ（ディレクトリ）のパスを文字列で指定しています。
# 今後、他のフォルダを処理したい場合は、ここを書き換えるだけでOKです。

# 指定フォルダ内の .xlsx ファイルをすべて取得
excel_files = glob.glob(os.path.join(folder_path, "sales_*.xlsx"))

# 「指定したフォルダ内の “sales_” で始まり、“.xlsx” で終わるファイルを全部取得」
# os.path.join() はフォルダ名とファイル名を安全に連結する関数。
# → "samplecode/excel_merge/sales_*.xlsx" という文字列を作ります。

# glob.glob(パターン) はワイルドカード検索。
# → "sales_*.xlsx" の「*」が「なんでもOK」の意味です。

# たとえばフォルダに以下があれば：

# sales_2024_01.xlsx
# sales_2024_02.xlsx
# sales_2024_03.xlsx

# この3つが excel_files というリストに格納されます。

# 💡補足
# Python の glob は「現在の作業ディレクトリ（カレントディレクトリ）」からの相対パスで探します。
# なので、スクリプトの場所と、実行している場所（ターミナルのカレントパス）がズレていると、ファイルが見つからなくなります。

print(f"📂 対象ファイル数: {len(excel_files)} 件")

# 読み込んだデータを格納するリスト
all_data = []

# 「これから読み込む各Excelのデータを順に入れていく空箱（リスト）を準備」
# あとで pd.concat() で全部まとめるための準備です。

# 各ファイルを順番に処理
for file in excel_files:
    df = pd.read_excel(file)
    df["元ファイル名"] = os.path.basename(file)  # ファイル名を追加
    all_data.append(df)

# 💡 処理の流れ
# for file in excel_files:
# → 取得したファイルを1つずつ順番に取り出す。

# pd.read_excel(file)
# → ExcelファイルをDataFrame（表形式）として読み込み。

# df["元ファイル名"] = os.path.basename(file)
# → 各行に「このデータはどのファイルから来たのか」を記録する列を追加。
# os.path.basename() はファイルパスから「ファイル名だけ」を抽出。
# 例： "samplecode/excel_merge/sales_2024_01.xlsx" → "sales_2024_01.xlsx"

# all_data.append(df)
# → 読み込んだ1つ分の表をリスト all_data に追加。

# すべてのデータを結合
merged_df = pd.concat(all_data, ignore_index=True)

# 「all_data に入っている3つのDataFrameを上下に結合する」

# pd.concat() は「連結」の関数。
# ignore_index=True にすることで、
# 元のインデックス番号（0,1,2...）を無視して新しく振り直します。
# 結果的に、3か月分のデータが1つの表にまとまります。

merged_df = merged_df.sort_values("月").reset_index(drop=True)

# sort_values("月") で「月」列を基準に昇順（1→2→3）に並び替え
# reset_index(drop=True) でインデックス番号を振り直す

# 出力ファイルパス
output_file = os.path.join(folder_path, "merged_sales.xlsx")

# 「結合結果をこのファイル名で出力するよ」
# ここでも os.path.join() を使うことで、
# どんなOS（Windows/Mac）でも安全にパスを作れます。

# Excel出力
merged_df.to_excel(output_file, index=False)

# 「merged_df の内容を Excelファイルとして保存」
# index=False にすると、DataFrameの左端の番号列（インデックス）を出力しません。

print("✅ 複数ファイルの結合が完了しました！")
print(f"出力ファイル: {output_file}")

# 処理が正常に終わったことを知らせるログを出力。
# ターミナルで進捗を確認できるようにしておくのは、
# 実務でもかなり重要なポイントです。


# ✅ まとめ（コード全体の流れ）
# 📥 glob で対象Excelを一括取得
# 📊 pandas で1つずつ読み込み
# 🧩 concat() で統合
# 💾 to_excel() で1ファイルに出力

# この一連の処理が「os / glob を使った複数Excelの一括処理」です。
