# mathモジュールを用いる
import math
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def lcm (x,y) :
  # ({{xにyを掛けた値}})の組をmath.gcd(x,y)で割った商を関数出力とする
  return (x*y)//math.gcd(x,y)
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# lcm(aの最初値,a(1))をxとする
x = lcm(a[0],a[1])
# 2をiとする
i = 2
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # lcm(x,a(i))をxとする
  x = lcm(x,a[i])
# xを出力する
print(x)