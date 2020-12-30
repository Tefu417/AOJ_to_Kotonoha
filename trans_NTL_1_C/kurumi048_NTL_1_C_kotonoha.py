# fractionsモジュールを用いる
import fractions
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def lcm (a,b) :
  # aにbを掛けた値をfractions.gcd(a,b)で割った商を関数出力とする
  return a*b//fractions.gcd(a,b)
# 入力された文字列の整数値をNとする
N = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# aの最初値をfとする
f = a[0]
# '1からN未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1,N) :
  # lcm(f,a(i))をfとする
  f = lcm(f,a[i])
# fを出力する
print(f)