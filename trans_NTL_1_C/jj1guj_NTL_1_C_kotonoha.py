# mathモジュールを用いる
import math
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def lcm (a,b) :
  # aにbを掛けた値をmath.gcd(a,b)で割った商を関数出力とする
  return a*b//math.gcd(a,b)
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# aの最初値をresultとする
result = a[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1,n) :
  # lcm(result,a(i))をresultとする
  result = lcm(result,a[i])
# resultを出力する
print(result)