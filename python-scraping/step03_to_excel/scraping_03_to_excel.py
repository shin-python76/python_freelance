# scraping_03_to_excel.py
# Step03：スクレイピング結果をExcelに出力する

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# =========================================
# ① HTML取得
# =========================================
url = "https://books.toscrape.com/"
response = requests.get(url)

# 「Books to Scrape」は練習用サイト。商用利用禁止ですが学習目的ならOK。
#  本番案件ではここに「企業の製品ページ」「不動産情報」「求人データ」などが入ります。

print("Status Code:", response.status_code)
soup = BeautifulSoup(response.text, "html.parser")

# response.text はページ全体のHTML文字列。
# BeautifulSoup() でHTMLを「ツリー構造」に変換。
# "html.parser" はPython標準のHTMLパーサー。軽量で学習には最適。

# 💡豆知識
#  他に "lxml" などの高速パーサーもあります。商用案件ではこちらを指定することが多いです。


# =========================================
# ② 書籍タイトルと価格を抽出
# =========================================
titles = [h3.get_text() for h3 in soup.find_all("h3")]

# 「Â£」を「£」に変換して文字化けを防止
prices = [
    p.get_text().replace("Â", "") for p in soup.find_all("p", class_="price_color")
]

# 🔹 ポイント
# .find_all("h3") → <h3> タグをすべて抽出（＝書籍タイトル）。
# .find_all("p", class_="price_color") → <p class="price_color"> を抽出（＝価格）。
# .get_text() → タグの中身の文字列だけを取得。
# .replace("Â", "") → 文字化けした「Â」を削除して「£」を正しく表示。

# 💡実務Tip
# HTML構造を確認して、必要なクラス名・タグ名を探すことがスクレイピングのコツ。
# （例：div class="product_name" や span class="price" など）


# =========================================
# ③ DataFrameに整理
# =========================================
df = pd.DataFrame({"書籍タイトル": titles, "価格": prices})

# 🔹 ポイント
# pandas.DataFrame() は表形式データを扱うクラス。
# 列名を日本語にすることで、Excel出力時にそのままヘッダーとして反映されます。
# 行数は、HTMLから抽出したタイトル・価格の件数に自動で合わせてくれます。

# 💡実務Tip
#  ここで len(titles) と len(prices) を比較して数が一致しているか確認するのも良い習慣です。

# =========================================
# ④ 出力フォルダとExcelファイル名を指定
# =========================================
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "books_data.xlsx")

# os.makedirs() はフォルダを作成する関数。
# exist_ok=True を指定することで、すでに存在してもエラーにならずスキップ。
# こうすることで、納品フォルダを常にクリーンに管理できる。
# os.path.join() → OSに依存しない安全なパス生成。

# 👉 実務的には「output」や「reports」などの出力専用ディレクトリを自動生成しておくのが基本です。

# =========================================
# ⑤ Excelに出力
# =========================================
df.to_excel(output_path, index=False, engine="openpyxl")
print(f"✅ Excelファイルを出力しました: {output_path}")

# 🔹 ポイント
# to_excel() → openpyxl エンジンでExcelファイルを作成。
# index=False → 行番号を出力しない。
# （Excelの1列目が自動的にID列になるのを防ぐ）

# 💡実務Tip
# 納品用のファイル名を動的にしたい場合は、

# output_file = os.path.join(output_folder, f"books_data_{pd.Timestamp.now():%Y%m%d}.xlsx")

# のように日付を埋め込むと便利です。


# =========================================
# ⑥ 実行確認用メッセージ
# =========================================
print("✅ 書籍データをExcelに出力しました！")
print(f"出力先: {output_file}")

# 🔹 ポイント
# ログ出力として、処理完了を明示。
# 実務では「クライアント確認用ログ」としても非常に重要。
