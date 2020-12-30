# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x, y  = map(int,input().split())
# xがyより小さいとき、
if x < y :
  # (yとx)の組を(xとy)の組とする
  (x, y) = (y, x)
# 1の間、繰り返す
while 1 :
  # yが0のとき、
  if y == 0 :
    # xを出力する
    print(x)
    # 繰り返すのを中断する
    break
  # xをyで割った余りをzとする
  z = x % y
  # zをxとする
  x = z
  # (yとx)の組を(xとy)の組とする
  (x, y) = (y, x)