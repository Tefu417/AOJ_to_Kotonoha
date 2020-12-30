# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x,y  = map(int, input().split())
# 真の間、繰り返す
while True :
  # xがyより小さいとき、
  if x<y :
    # yをzとする
    z = y
    # xをyとする
    y = x
    # zをxとする
    x = z
  # xをyで割った余りをkとする
  k = x%y
  # kが0のとき、
  if k==0 :
    # 繰り返すのを中断する
    break
  # yをxとする
  x = y
  # kをyとする
  y = k
# yを出力する
print(y)