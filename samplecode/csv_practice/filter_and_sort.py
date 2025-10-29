import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("sample.csv")

# === ① 特定の列を抽出 ===
print("🟢 部署と給与の列だけを抽出")
print(df[["部署", "給与"]])
print("-" * 40)

# 複数列を [[ ]] の二重括弧で指定します。

# === ② 条件に合う行だけを抽出 ===
print("🟡 営業部のデータだけ抽出")
sales = df[df["部署"] == "営業"]
print(sales)
print("-" * 40)

# “部署が営業の行だけ” を取り出しています。
#  条件式（==, >, <, !=など）を自由に使えます。

# === ③ 並び替え ===
print("🔵 年齢順に並び替え")
sorted_df = df.sort_values("年齢")
print(sorted_df)
print("-" * 40)

# 年齢を昇順（小さい順）に並べます。
# 降順にしたい場合は ascending=False をつけます。

# === ④ 新しい列を追加 ===
print("🟣 年収（給与×12）を追加")
df["年収"] = df["給与"] * 12
print(df)
print("-" * 40)

# Excelの「年収＝給与×12」と同じ考え方。
# df["新しい列名"] = ... → 新しい列を追加する
# DataFrameでは列ごとに一括計算できます。

# === ⑤ 列を削除（例） ===
print("🔴 年齢列を削除")
df_drop = df.drop(columns=["年齢"])
print(df_drop)

# その列を削除した新しいDataFrameを作ります（元のdfは変わりません）。
