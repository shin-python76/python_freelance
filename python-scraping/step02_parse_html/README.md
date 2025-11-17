# 🧩 Step02：BeautifulSoupでHTMLを解析し要素を抽出

## 🎯 学習目的
- BeautifulSoupを使ってHTMLから特定のタグ・要素を取得する
- `.find_all()` や `.text` を理解して、構造化データを扱えるようになる

---

## 🧠 使用ライブラリ
- `requests`：WebページのHTMLを取得
- `beautifulsoup4`：HTML解析用ライブラリ（タグの抽出に使用）

---

## 🧾 実行ファイル
`scraping_02_parse_basic.py`

---

## 💻 主な処理内容
1. Webサイト（Books to Scrape）からHTMLを取得  
2. BeautifulSoupでHTMLを解析 (`BeautifulSoup(response.text, "html.parser")`)  
3. `<h3>` タグで書籍タイトルを抽出  
4. `<p class="price_color">` で価格情報を抽出  
5. `.text` を用いてタグ内の文字列を取得  

---

## ✅ 出力例

