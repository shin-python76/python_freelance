import pandas as pd

df = pd.read_csv("/Users/kobayashishinya/Desktop/sample.csv")
print(df.head())


# pandas は「データ分析・集計」のための超有名ライブラリ。
# これを使うことで、Excelのような表データをPython上で扱えるようになります。
# as pd は「別名をつけて呼び出す」という指定で、
# 以降は pandas ではなく短く pd と書けるようになります。

# df = pd.read_csv("/Users/kobayashishinya/Desktop/sample.csv")
# 「pandasを使ってCSVファイルを読み込み、df という変数に格納する」
# pd.read_csv() は pandas の中の関数（メソッド）です。
# 👉 “read CSV（CSVを読む）” の意味。
# 引数 "..." の中に、ファイルのパス（場所）を指定します。

# print(df.head())
# 「DataFrame の最初の5行を表示する」
# .head() は “頭のほう” を見る関数。
# デフォルトで5行を表示します。
# df.head(3) のように、括弧内に数字を指定すれば表示行数を変えられます。

# 補足：DataFrameとは？
# df は 「表（テーブル）」のようなデータ構造 です。
# ExcelのシートをPythonの中に再現したようなものです。
# pandasでは、このDataFrameに対して：
# 特定の行／列を抽出、並び替え、集計（平均・合計など）、統計分析、といった操作が可能になります。
