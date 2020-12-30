[#Document [# '-*- coding: utf-8 -*-']]
# [#MultiString '"\nElementary Number Theory - Least Common Multiple\nhttp://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_C&lang=jp\n\n"']
"
Elementary Number Theory - Least Common Multiple
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_C&lang=jp

"
# sysモジュールを用いる
import sys[#FromDecl name: [#ModuleName 'math']names: [# [#Name 'gcd']]][#FromDecl name: [#ModuleName 'functools']names: [# [#Name 'reduce']]]
# 関数solveを[#FuncParam [#ParamDecl name: [#Name 'A']]]のパラメータを持つように定義する
def solve (A) :
  # reduce([#FuncExpr params: [#Param [#Name 'x'][#Name 'y']]body: [#Infix left: [#Infix left: [#Name 'x']name: [#Name '*']right: [#Name 'y']]name: [#Name '//']right: [#ApplyExpr name: [#Name 'gcd']params: [#Arguments [#Name 'x'][#Name 'y']]]]],A)を関数出力とする
  return reduce(lambda x, y: x * y // gcd(x, y), A)
# 関数mainを[#FuncParam [#ParamDecl name: [#Name 'args']]]のパラメータを持つように定義する
def main (args) :
  # 入力された文字列を_とする
  _ = input()
  # {{入力された文字列を空白で分割した列}}の各要素をaとし、aの整数値の列をAとする
  A = [int(a) for a in input().split()]
  # solve(A)をansとする
  ans = solve(A)
  # ansを出力する
  print(ans)
# 識別子が'__main__'のとき、
if __name__ == '__main__' :
  # main(sys.argvの先頭を除いた部分)
  main(sys.argv[1:])