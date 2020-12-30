# mathモジュールを用いる
import math[#FromDecl name: [#ModuleName 'functools']names: [# [#Name 'reduce']]]
# 関数lcm_baseを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def lcm_base (x,y) :
  # ({{xにyを掛けた値}})の組をmath.gcd(x,y)で割った商を関数出力とする
  return (x*y)//math.gcd(x,y)
# 関数lcm_listを[#FuncParam [#ParamDecl name: [#Name 'numbers']]]のパラメータを持つように定義する
def lcm_list (numbers) :
  # reduce(lcm_base,numbers,1)を関数出力とする
  return reduce(lcm_base,numbers,1)
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# lcm_list(a)を出力する
print(lcm_list(a))