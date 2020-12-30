# 入力された文字列を空白で分割した列をLとする
L = input().split( )
# Lの最初値の整数値をxとする
x = int(L[0])
# L(1)の整数値をyとする
y = int(L[1])
# xがyより小さいとき、
if x<y :
  # xをwとする
  w = x
  # yをxとする
  x = y
  # wをyとする
  y = w
# xをyで割った余りが0と等しくない間、繰り返す
while x%y!=0 :
  # yをwとする
  w = y
  # xをyで割った余りをyとする
  y = x%y
  # wをxとする
  x = w
# yを出力する
print(y)