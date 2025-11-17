# scraping_02_parse_basic.py
# ========================================
# BeautifulSoupを使ってHTMLから特定要素を抽出する練習
# ========================================

import requests
from bs4 import BeautifulSoup

# BeautifulSoup
# → 取得したHTMLの「タグ構造」を理解し、
# 必要な部分（タイトル・価格など）を抜き出すツール。
# HTMLを“データベースのように検索できる”ようにしてくれます。

# 1️⃣ 練習用サイト（安全にスクレイピング可能）
url = "https://books.toscrape.com/"

# 2️⃣ HTMLを取得
response = requests.get(url)

# ステータスコード確認
print("Status Code:", response.status_code)

# requests.get(url)
# → 指定したURLにアクセスしてHTMLを取得します。

# response オブジェクトには次の情報が含まれています：
# .status_code: サーバーの応答コード（200なら成功）
# .text: HTML全体（文字列データ）
# .content: HTMLをバイト列で保持（画像などの取得に使う）


# 3️⃣ BeautifulSoupでHTMLを解析
soup = BeautifulSoup(response.text, "html.parser")

# response.text：取得したHTML全体の文字列。
# "html.parser"：Python標準のHTML解析エンジン。
# 他にも "lxml" などがありますが、標準のもので十分。

# 💡 イメージ：
# この一行で「ただの文字列HTML」が、
# “Pythonが理解できるHTMLツリー構造”に変わります。


# 4️⃣ ページタイトルを取得（<title>タグ）
page_title = soup.title.text
print("📘 ページタイトル:", page_title)

# soup.title：<title>タグ全体を取得。
# → <title>All products | Books to Scrape - Sandbox</title>
# .text：タグの中の文字列だけを取り出す。


# 5️⃣ 書籍タイトル一覧を取得
# サイト内の「<h3>」タグにタイトルが入っている
books = soup.find_all("h3")

print("\n=== 書籍タイトル一覧（上位5件） ===")
for book in books[:5]:
    print("-", book.text)

# .find_all("h3")
# → <h3> タグをすべてリスト形式で取得。
# → 各書籍タイトルが <h3> 内にあるため、これで一覧が取れる。

# .text
# → HTMLタグを除いたテキストだけを取得。
# books[:5]
# → 取得結果のうち先頭5件のみを表示（確認用）。


# 6️⃣ 特定の要素（価格）を取得してみる
prices = soup.find_all("p", class_="price_color")

print("\n=== 価格情報（上位5件） ===")
for price in prices[:5]:
    print("-", price.text)

# .find_all("p", class_="price_color")
# → HTML内の <p> タグのうち、
# class="price_color" が付いた要素のみを取得。


# ✅ ここまでで：
# - requestsでHTMLを取得
# - BeautifulSoupでタグを抽出
# - find_all()で複数要素を取得
# - .textでテキスト内容を取り出す
