[#Document [# 'coding: utf-8']][#Document [# 'Your code here!']][#FromDecl name: [#ModuleName 'math']names: [# [#Name 'gcd']]][#FromDecl name: [#ModuleName 'functools']names: [# [#Name 'reduce']]]
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def lcm (x,y) :
  # xにyを掛けた値をgcd(x,y)で割った商を関数出力とする
  return x*y//gcd(x,y)
# reduce(lcm,a)を出力する
print(reduce(lcm,a))