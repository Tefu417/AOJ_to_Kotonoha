[#Document [# 'coding: utf-8']][#Document [# 'Your code here!']]
# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x,y = map(int,input().split())
# (xとy)からなる列をソートした列を展開し順にxとyとする
x,y = sorted([x,y])
# xをyで割った余りが0と等しくない間、繰り返す
while x%y!=0 :
  # yとxをyで割った余りをxとyとする
  x,y = y,x%y
# yを出力する
print(y)