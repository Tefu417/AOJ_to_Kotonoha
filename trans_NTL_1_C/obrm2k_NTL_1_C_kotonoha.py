# mathモジュールを用いる
import math
# 入力された文字列の整数値をnとする
n = int(input())
# 1をxとする
x = 1
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストの各要素を順にyとして、繰り返す
for y  in list(map(int,input().split())) :
  # yにxを掛けた値をmath.gcd(y,x)で割った商をxとする
  x = y*x // math.gcd(y,x)
# xを出力する
print(x)