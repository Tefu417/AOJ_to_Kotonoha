[#FromDecl name: [#ModuleName 'enum']names: [# [#Name 'Enum']]]
# sysモジュールを用いる
import sys
# mathモジュールを用いる
import math
# 2000000000をBIG_NUMとする
BIG_NUM = 2000000000
# 1000000007をMODとする
MOD = 1000000007
# 0.000000001をEPSとする
EPS = 0.000000001
# 関数calc_gcdを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def calc_gcd (a,b) :
  # aがbより小さいとき、
  if a < b :
    # aとbを入れ替える
    a, b = b, a
  # bが0のとき、
  if b == 0 :
    # aを関数出力とする
    return a
  # calc_gcd(b,aをbで割った余り)を関数出力とする
  return calc_gcd(b,a%b)
# map(整数,入力された文字列を空白で分割した列)を展開し順にAとBとする
A,B  = map(int,input().split())
# "%d"を(calc_gcd(A,B))の組で割った余りを出力する
print("%d"%(calc_gcd(A,B)))