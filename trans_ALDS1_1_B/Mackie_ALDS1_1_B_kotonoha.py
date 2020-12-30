# 入力された文字列を空白で分割した列をaとする
a = input().split()
# aの最初値の整数値をxとする
x = int(a[0])
# a(1)の整数値をyとする
y = int(a[1])
# yの間、繰り返す
while y :
  # yとxをyで割った余りをxとyとする
  x, y  = y, x%y
# xを出力する
print(x)