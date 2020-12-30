# mathモジュールを用いる
import math
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# aの最初値をlcmとする
lcm = a[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1,n) :
  # lcmをxとする
  x = lcm
  # a(i)をyとする
  y = a[i]
  # ({{xにyを掛けた値}})の組をmath.gcd(x,y)で割った商をlcmとする
  lcm = (x*y)//math.gcd(x,y)
# lcmを出力する
print(lcm)