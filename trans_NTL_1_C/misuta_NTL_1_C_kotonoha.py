# mathモジュールを用いる
import math
# 関数calc_LCMを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def calc_LCM (x, y) :
  # math.gcd(x, y)をzとする
  z = math.gcd(x, y)
  # xにyを掛けた値をzで割った商をansとする
  ans = x*y//z
  # ansを関数出力とする
  return ans
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをlstとする
lst = list(map(int, input().split()))
# 1をsとする
s = 1
# lstの各要素を順にiとして、繰り返す
for i  in lst :
  # calc_LCM(s,i)をsとする
  s = calc_LCM(s, i)
# sを出力する
print(s)