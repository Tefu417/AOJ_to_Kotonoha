# mathモジュールを用いる
import math
# 入力された文字列
input()
# 1をbとする
b = 1
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストの各要素を順にiとして、繰り返す
for i  in list(map(int,input().split())) :
  # iにbを掛けた値をmath.gcd(i,b)で割った商をbとする
  b = i*b//math.gcd(i,b)
# bを出力する
print(b)