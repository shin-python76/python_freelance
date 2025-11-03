import pandas as pd

# CSVファイルの読み込み
df = pd.read_csv("sales_data.csv")

# 日付をdatetime型に変換
df["日付"] = pd.to_datetime(df["日付"])

# 月を抽出
df["月"] = df["日付"].dt.month

# CSVから読み込んだデータフレーム df の「日付」列を取り出しています。
# .dt 👉 datetime 型のデータにアクセスするための**アクセサ（dt accessor）**です。
# pandasでは、「日付データ」から年月日・曜日などを抽出する際に .dt を使います。
# これは、datetime オブジェクトにおける .month, .year, .day と同じ考え方です。

# 月ごとに売上金額を集計
monthly_sales = df.groupby("月")["売上金額"].sum().reset_index()

# 結果をExcelに出力
output_file = "月別売上集計.xlsx"
monthly_sales.to_excel(output_file, index=False)

# .to_excel(...)　👉 DataFrame を Excelファイル（.xlsx）形式で書き出すメソッドです。
# pandasには同様の出力メソッドがいくつかあります👇
# メソッド	出力形式
# to_csv()	CSV
# to_excel()	Excel (.xlsx)
# to_json()	JSON
# to_html()	HTMLテーブル
# つまり .to_excel() は、「Excelに保存する命令」。

# index=False 👉 Excelに インデックス（行番号）を書き出さない ようにするオプションです。
# pandasのDataFrameには、自動的に「0,1,2,…」という行番号（index）がついていますが、
# それを出力すると、Excelではこうなってしまいます👇

#   月	売上金額
# 0	1	  450
# 1	2	  700
# 2	3	  900

# → この左端の 0,1,2 は分析には不要なので、index=False で削除しています。

print("✅ 月別売上集計.xlsx を出力しました！")
