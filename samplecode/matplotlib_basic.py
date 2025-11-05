# samplecode/matplotlib_basic.py
import matplotlib.pyplot as plt

# matplotlib ライブラリの中の pyplot モジュールを読み込みます。
# グラフ描画のための関数（plot(), bar(), show()など）が含まれており、
# plt という短縮名で使うのが一般的です。
# 👉 Excelで言うと「グラフ作成ツール」を呼び出した状態です。

# 日本語フォントを設定（Mac用）
plt.rcParams["font.family"] = "Hiragino Sans"

# macOS では 'Hiragino Sans' が最も安全で綺麗に日本語を表示できます。
# これを設定しないと、UserWarning: Glyph missing... が出てしまうことがあります。

# データを用意
months = ["1月", "2月", "3月", "4月", "5月"]
sales = [100, 150, 130, 170, 200]

# グラフに表示するデータです。
# months が X軸、sales が Y軸になります。
# Pythonのリスト形式（[ ]）で作成しています。
# 👉 Excelで言えば、「月」「売上」列のデータ部分にあたります。

# 折れ線グラフを描画
plt.plot(months, sales, color="blue", marker="o", linestyle="-")

# 折れ線グラフを描く関数です。

# 引数	意味
# months	X軸の値（横軸）
# sales	Y軸の値（縦軸）
# color='blue'	線の色
# marker='o'	各点に丸印を付ける
# linestyle='-'	実線（他に '--' 点線、':' 破線 など）

# タイトルと軸ラベル
plt.title("月別売上推移")
plt.xlabel("月")
plt.ylabel("売上（万円）")

# plt.title('月別売上推移')
# グラフ全体のタイトルを設定します。

# plt.xlabel('月'), plt.ylabel('売上（万円）')
# X軸とY軸のラベルを設定します。
# (万円) のように単位も入れると実務的に分かりやすくなります。

# グリッド線を追加
plt.grid(True)

# 背景に補助線（グリッド線）を表示します。
# データの増減が視覚的に読み取りやすくなります。

# グラフを表示
plt.show()

# グラフを画面に表示します。
# この1行がないとウィンドウが開きません!!

# 棒グラフの描画
plt.bar(months, sales, color="orange")

# plt.bar() は 縦棒グラフ（Vertical Bar Chart） を描く関数です。
# X軸の値ごとに、Y軸の値を高さとして棒を描画します。

# タイトルと軸ラベル
plt.title("月別売上金額（棒グラフ）")
plt.xlabel("月")
plt.ylabel("売上（万円）")

# グラフを表示
plt.show()

# plt.show() はグラフを区切る役割
# plt.show() を呼ぶと、一度グラフを「リセット」します。
# なので上のように plot() → show() → bar() → show() と書くと、
# 2つのグラフが別々のウィンドウで表示されます。

# ✅ 2. もし「同じ図に重ねたい」場合
# 棒グラフと折れ線を同一グラフに重ねる場合は、
# show() の前で両方を描けばOKです👇
