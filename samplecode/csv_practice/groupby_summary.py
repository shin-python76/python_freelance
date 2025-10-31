import pandas as pd

# CSVを読み込み
df = pd.read_csv("sample_sales.csv")

# === 日付列から「月」を抽出 ===
df["月"] = pd.to_datetime(df["日付"]).dt.month

# df["日付"]	CSV内の「日付」列を取り出す（文字列として扱われている）
# pd.to_datetime(...)	日付文字列を “日付データ型（datetime）” に変換する
# → pandasが「日時型（datetime64）」に変換しました。(例：2025-01-05 00:00:00)
# これで年月日を自在に分解できるようになります。
# .dt.month	日付データから「月の数値（1〜12）」だけを取り出す
# df["月"] = ...	その結果を新しい列「月」として追加する

print("=== データ確認 ===")
print(df)
print("-" * 40)

# === ① 部署ごとの売上平均 ===
print("① 部署ごとの平均売上")
dept_mean = df.groupby("部署")["売上"].mean()
print(dept_mean)
print("-" * 40)

# groupby() → 指定列でグループ化
# [列名] → 集計対象を選ぶ
# .mean() → 平均値を出す（.sum() なら合計）

# === ② 部署ごとの売上合計 ===
print("② 部署ごとの売上合計")
dept_sum = df.groupby("部署")["売上"].sum()
print(dept_sum)
print("-" * 40)

# === ③ 月ごとの売上合計 ===
print("③ 月ごとの売上合計")
month_sum = df.groupby("月")["売上"].sum()
print(month_sum)
print("-" * 40)

# === ④ 部署 × 月ごとの売上合計 ===
print("④ 部署 × 月ごとの売上合計")
dept_month_sum = df.groupby(["部署", "月"])["売上"].sum()
print(dept_month_sum)
print("-" * 40)

# === ⑤ ピボットテーブル形式に変換 ===
print("⑤ ピボットテーブル表示")
pivot = pd.pivot_table(df, index="部署", columns="月", values="売上", aggfunc="sum")
print(pivot)

# index="部署"	行（縦軸）に使う項目	営業・開発・総務
# columns="月"	列（横軸）に使う項目	1, 2, 3（月）
# values="売上"	集計対象のデータ	売上金額
# aggfunc="sum"	集計方法	合計を求める（他に平均＝meanなども可）

# 🧮 aggfunc で集計方法を変える
# 目的	設定例	結果
# 平均を出す	aggfunc="mean"	部署×月ごとの平均売上
# 最大値を出す	aggfunc="max"	部署×月ごとの最大売上
# 複数集計	aggfunc=["sum", "mean"]	合計と平均を両方表示
