[#Document [# 'coding: utf-8']][#Document [# 'Your code here!']]
# mathモジュールを用いる
import math
# 入力された文字列の整数値をnとする
n = int(input())
# 1をbとする
b = 1
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストの各要素を順にaとして、繰り返す
for a  in list(map(int,input().split())) :
  # aにbを掛けた値をmath.gcd(a,b)で割った商をbとする
  b = a*b // math.gcd(a,b)
# bを出力する
print(b)