# 🧩 Step03：スクレイピング結果をExcelに出力する

## 💻 使用ライブラリ
| ライブラリ | 役割 |
|-------------|------|
| `requests` | WebページのHTMLを取得 |
| `beautifulsoup4` | HTMLを解析してタグを抽出 |
| `pandas` | データを表形式に整形 |
| `openpyxl` | Excelファイルの作成・保存 |

---

## 📁 実行ファイル

scraping_03_to_excel.py

---

## 🧠 主な処理内容

1. Webサイト（[Books to Scrape](https://books.toscrape.com/)）からHTMLを取得  
2. `BeautifulSoup` でHTMLを解析  
3. `<h3>` タグで書籍タイトルを抽出  
4. `<p class="price_color">` タグで価格を抽出  
5. 抽出データを `pandas.DataFrame` に整形  
6. `openpyxl` エンジンを使ってExcelファイルに出力  

---

## ✅ 出力ファイル

output/books_data.xlsx



## 📊 出力例（Excelプレビュー）

| 書籍タイトル | 価格 |
|--------------|------|
| A Light in the ... | £51.77 |
| Tipping the Velvet | £53.74 |
| Soumission | £50.10 |
| Sharp Objects | £47.82 |
| Sapiens: A Brief History ... | £54.23 |

---

## 📝 ポイント
- BeautifulSoup × pandas × openpyxl の連携で「案件形式」の完成形に。  
- Excel納品できる形に整えることで、スクレイピング案件への応用が可能。  
- 出力フォルダ（`output`）を自動生成する仕組みも実装済み。  

---

## 🚀 今後の展開
次のステップでは、  
複数ページを自動巡回して **全書籍データを収集する「模擬案件④」** に進みます！
