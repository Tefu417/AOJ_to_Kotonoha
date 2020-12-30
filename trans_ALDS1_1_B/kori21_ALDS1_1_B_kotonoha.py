# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x, y  = map(int, input().split())
# xがyより大きいとき、
if x > y :
  # xとyを入れ替える
  x, y = y, x
# xをyで割った余りが0と等しくない間、繰り返す
while x % y != 0 :
  # yとxをyで割った余りをxとyとする
  x, y  = y, x % y
# yを出力する
print(y)