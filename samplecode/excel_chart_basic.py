# samplecode/excel_chart_basic.py
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

# 1️⃣ from openpyxl.chart import ... とは？
# openpyxl には、いくつかの機能モジュールがあります。

# モジュール名	役割
# openpyxl	Excel全体の基本操作（読み書きなど）
# openpyxl.styles	セルの装飾（フォント、色、罫線など）
# openpyxl.chart	グラフ（Chart）関連の操作

# つまりこの行は、
# 「openpyxlの中の chart モジュールから、特定のクラスを取り出す」
# という意味になります。

# 2️⃣ BarChart：棒グラフを作るためのクラス
# 📘 概要
# Excelの「挿入 → 棒グラフ」と同じものをPythonで作るためのクラスです。
# BarChart() でインスタンスを作成すると、棒グラフの「枠」が生成されます。

# 3️⃣ Reference：グラフの元データ（セル範囲）を指定するクラス
# 📘 概要
# Reference() は、Excelシート上のセル範囲を参照するためのオブジェクトを作ります。
# これが「グラフの元になるデータ」や「横軸ラベル」となります。

# Excelファイルを新規作成
wb = Workbook()
ws = wb.active
ws.title = "売上データ"

# 見出し
ws.append(["月", "売上", "利益"])

# ワークシート（ws）に1行を追加 する命令です。
# append() は「リスト（[]）」で渡した内容を 行単位で追加 します。
# つまり、
# ["月", "売上", "利益"]
# が →
# Excel上では A1, B1, C1 にそれぞれ書き込まれます。

# A列	B列	C列
# 月	売上	利益

# 📘 これはExcelでいう「1行目の見出し（ヘッダー）」を作っている部分です。

# データ
data = [
    ["1月", 100, 20],
    ["2月", 150, 30],
    ["3月", 130, 25],
    ["4月", 170, 35],
    ["5月", 200, 50],
]

# ここで、複数行のデータ をリストの中にまとめています。
# 各行をさらに小さなリストで表しています。

# data = [
# ["1月", 100, 20],  # ← A2〜C2 に入る
# ["2月", 150, 30],  # ← A3〜C3 に入る
#    ...
# ]
# つまり、data は「2次元リスト（リストの中にリスト）」です。
# この構造が、Excelの「行と列」にちょうど対応しています。

# データ構造	内容	結果
# ✅ 2次元リスト（推奨）	[["1月",100,20], ["2月",150,30]]	各リストが1行になる（表形式）
# ❌ 1次元リスト	["1月",100,20,"2月",150,30]	縦1列に書き込まれる
# ⚙️ forなしでappend連打	ws.append(["1月",100,20]) …	手動で1行ずつ書く必要あり

# 💬 実務的な視点でのまとめ
# 2次元リスト形式 は「表データ」を表すのに最適。
# CSV・データベース・APIレスポンスもだいたいこの形。
# そのため for row in data: の形が最も汎用的で、
# ExcelやCSVへの出力・分析処理でも使い回せます。

for row in data:
    ws.append(row)

# for row in data:
# data には 5 つの小リスト（行データ）が入っています。
# for 文を使うことで、1行ずつ順番に取り出します。

# ループ回数	row の中身	追加先（Excel）
# 1回目	["1月", 100, 20]	2行目（A2〜C2）
# 2回目	["2月", 150, 30]	3行目（A3〜C3）
# 3回目	["3月", 130, 25]	4行目（A4〜C4）
#  …	…	…

# ws.append(row)
# row の内容（例：["1月", 100, 20]）を1行としてシートに書き込みます。
# append() は自動的に「次の空いている行」に追加します。

# つまり：dataの中のすべての行を順番にExcelに追加していく、という処理です。


# ===== 📊 棒グラフを埋め込む処理 =====
# openpyxl.chart モジュールを使うことで、Excel内にネイティブなグラフを作成できます。

chart = BarChart()  # 棒グラフオブジェクトを生成
chart.title = "月別売上グラフ"
chart.x_axis.title = "月"
chart.y_axis.title = "売上（万円）"

# グラフで使用するデータ範囲を指定します。
# Reference(ws, min_col, max_col, min_row, max_row)
#   → min_col/max_col : グラフに使う列の範囲（ここでは「売上」列＝B列）
#   → min_row/max_row : 見出し行を含むデータ範囲（1行目〜6行目）

data_ref = Reference(ws, min_col=2, max_col=2, min_row=1, max_row=6)  # 売上列
cats_ref = Reference(ws, min_col=1, min_row=2, max_row=6)  # 月列

# グラフにデータを追加
chart.add_data(data_ref, titles_from_data=False)
chart.set_categories(cats_ref)

# 1️⃣ chart.add_data(data_ref, titles_from_data=False)
# 📘 概要
# add_data() は、
# グラフ（chart）に対して「どのセルの値を棒の高さ（データ）として使うか」を指定します。
# ここで渡している data_ref は、先ほど作った「セル範囲の参照」です👇
# data_ref = Reference(ws, min_col=2, max_col=2, min_row=2, max_row=6)
# これは B2〜B6 の範囲を意味しています。
# つまり、売上データ（100,150,130,170,200）です。

# 🧩 実際のイメージ
# A列	B列	C列
# 月	売上	利益
# 1月	100	20
# 2月	150	30
# 3月	130	25
# 4月	170	35
# 5月	200	50

# ここで data_ref が B2:B6 のデータを参照しているため、
# グラフ上では「1月〜5月の棒の高さ」としてこの値が使われます。

# 🟩 引数：titles_from_data=False
# これは「データ範囲の1行目を系列名（タイトル）として扱うか？」を決めるオプションです。

# 設定	意味	結果
# True	範囲の最初の行（または列）を系列名として扱う	見出しを“ラベル”として使う
# False	純粋に数値データだけ使う	データだけをグラフ化

# 今回の data_ref は B2:B6（見出しなし）なので、
# titles_from_data=False にするのが正解です。

# もし範囲を B1:B6（1行目に「売上」がある）とした場合は、
# titles_from_data=True にすることで「系列名：売上」が自動で反映されます。

# 🔍 実務での使い分け例
# データ範囲	titles_from_data	グラフ上の凡例
# B1:B6	True	「売上」と表示される
# B2:B6	False	凡例なし（単一データ系列）

# 2️⃣ chart.set_categories(cats_ref)
# 📘 概要
# グラフの 横軸（X軸）に表示するラベル を指定します。
# → 「1月」「2月」などの文字がここで設定されます。

# ここで渡している cats_ref はこう定義されています👇
# cats_ref = Reference(ws, min_col=1, min_row=2, max_row=6)
# つまり A2:A6 の範囲、すなわち「月」列です。

# 🧩 イメージ図
# A列	B列
# 1月	100
# 2月	150
# 3月	130
# 4月	170
# 5月	200

# このうち、
# add_data() → B列の数値（縦軸＝棒の高さ）
# set_categories() → A列の文字（横軸＝ラベル）
# をそれぞれ指定しているわけです。

# グラフをシートに追加（E列2行目の位置に配置）
ws.add_chart(chart, "E2")

# add_chart() は、
# openpyxlでシートにグラフを実際に貼り付けるためのメソッドです。

# 📘 意味：
# 「このシート（ws）に、作ったグラフ（chart）を貼り付けて、
# 配置開始セル（E2）を基準に表示する」

# つまり、E2セルの位置から右下方向にグラフが表示されます。
# 📊 イメージ図：
# A	B	C	D	E	F	G
# 1				📊 グラフの左上がE2から始まる

# 保存
wb.save("sales_chart.xlsx")
print("✅ Excelファイルを作成しました：sales_chart.xlsx")
