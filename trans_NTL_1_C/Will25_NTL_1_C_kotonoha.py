# mathモジュールを用いる
import math
# 関数LCMを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def LCM (x, y) :
  # ({{xにyを掛けた値}})の組をmath.gcd(x, y)で割った商を関数出力とする
  return (x * y) // math.gcd(x, y)
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# 1をlcmとする
lcm = 1
# aの各要素を順にaiとして、繰り返す
for ai  in a :
  # LCM(ai,lcm)をlcmとする
  lcm = LCM(ai,lcm)
# lcmを出力する
print(lcm)