# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def gcd (a, b) :
  # bの間、繰り返す
  while b :
    # bとaをbで割った余りをaとbとする
    a, b  = b, a % b
  # aを関数出力とする
  return a
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def lcm (a, b) :
  # aにbを掛けた値をgcd(a,b)で割った商を関数出力とする
  return a * b // gcd(a, b)
# functoolsモジュールを用いる
import functools
# 関数solveを[#FuncParam '()']のパラメータを持つように定義する
def solve () :
  # 入力された文字列をnとする
  n = input()
  # map(整数,入力された文字列を空白で分割した列)をnumsとする
  nums = map(int, input().split())
  # functools.reduce(lcm, nums)を出力する
  print(functools.reduce(lcm, nums))
# solve()
solve()