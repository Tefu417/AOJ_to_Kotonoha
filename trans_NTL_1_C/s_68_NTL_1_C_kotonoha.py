# mathモジュールを用いる
import math
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをLとする
L = list(map(int,input().split()))
# 空行を出力する
print
# nが1のとき、
if n==1 :
  # Lの最初値を出力する
  print(L[0])
# ()
else :[#Else [#Block [#VarDecl name: [#Name 'x']expr: [#IndexExpr recv: [#Name 'L']index: [#Int '0']]][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '1'][#Name 'n']]]body: [#Block [#VarDecl name: [#Name 'x']expr: [#Infix left: [#Tuple [#Infix left: [#Name 'x']name: [#Name '*']right: [#IndexExpr recv: [#Name 'L']index: [#Name 'i']]]]name: [#Name '//']right: [#MethodExpr recv: [#Name 'math']name: [#Name 'gcd']params: [#Arguments [#Name 'x'][#IndexExpr recv: [#Name 'L']index: [#Name 'i']]]]]][#SelfAssignment left: [#Name 'i']name: [# '+=']right: [#Int '1']]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'x']]]]]]