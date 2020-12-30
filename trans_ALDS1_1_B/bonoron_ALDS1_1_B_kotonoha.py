# [#MultiString '"import math\nx,y=map(int,input().split())\nprint(math.gcd(x,y))"']
"import math
x,y=map(int,input().split())
print(math.gcd(x,y))"
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをソートした列を展開し順にxとyとする
x,y = sorted(list(map(int,input().split())))
# xをrとする
r = x
# 1の間、繰り返す
while 1 :
  # xをyで割った余りが0のとき、
  if x%y==0 :
    # 繰り返すのを中断する
    break
  # xをyで割った余りをrとする
  r = x%y
  # yをxとする
  x = y
  # rをyとする
  y = r
# rを出力する
print(r)