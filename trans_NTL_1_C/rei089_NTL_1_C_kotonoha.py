# mathモジュールを用いる
import math[#FromDecl name: [#ModuleName 'functools']names: [# [#Name 'reduce']]]
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def lcm (x, y) :
  # ({{xにyを掛けた値}})の組をmath.gcd(x, y)で割った商を関数出力とする
  return (x * y) // math.gcd(x, y)
# 入力された文字列の整数値をnとする
n = int(input())
# map(整数,({{入力された文字列を空白で分割した列}})の組)をaとする
a = map(int,(input().split()))
# reduce(lcm,a)を出力する
print(reduce(lcm,a))