# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x, y  = map(int, input().split())
# yが0より大きい間、繰り返す
while y>0 :
  # yとxをyで割った余りをxとyとする
  x, y  = y, x%y
# xを出力する
print(x)