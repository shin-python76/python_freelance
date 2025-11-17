# 🕸️ Webスクレイピング基礎（Step1）

## 📘 学習目的
PythonでWebページのHTMLデータを取得する基本を学習。  
`requests` ライブラリを用いて、安全な練習サイトからHTMLを取得できるようになることが目的。

---

## 📦 使用ライブラリ
| ライブラリ | 用途 | 備考 |
|-------------|------|------|
| `requests` | Webサイトにアクセスし、HTMLを取得 | スクレイピングの基本中の基本 |

---

## 🧩 コード概要

```python
import requests

# 練習用サイト
url = "https://books.toscrape.com/"

# HTML取得
response = requests.get(url)

# ステータスコード確認
print("Status Code:", response.status_code)

# HTML冒頭500文字を出力
print("\n=== HTML Preview ===")
print(response.text[:500])
