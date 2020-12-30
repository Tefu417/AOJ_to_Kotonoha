[#FromDecl name: [#ModuleName 'functools']names: [# [#Name 'reduce']]]
# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def gcd (x,y) :
  # yの間、繰り返す
  while y :
    # yとxをyで割った余りをxとyとする
    x,y  = y,x%y
  # xを関数出力とする
  return x
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def lcm (x,y) :
  # xをgcd(x,y)で割った商にyを掛けた値を関数出力とする
  return x//gcd(x,y)*y
# 入力された文字列の整数値をNとする
N = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをAとする
A = list(map(int,input().split()))
# reduce(lcm,A)を出力する
print(reduce(lcm,A))