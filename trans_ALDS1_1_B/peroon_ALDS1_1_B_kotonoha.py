[#Document [# '-*- coding: utf-8 -*-']]
# sysモジュールを用いる
import sys
# osモジュールを用いる
import os
# mathモジュールを用いる
import math
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストを展開し順にaとbとする
a, b  = list(map(int, input().split()))[#Document [# 'a?????§?????????????????????']]
# bがaより大きいとき、
if b > a :
  # aとbを入れ替える
  a, b = b, a
# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def gcd (a, b) :
  # bが0のとき、
  if b == 0 :
    # aを関数出力とする
    return a
  # ()
  else :[#Else [#Block [#Return expr: [#ApplyExpr name: [#Name 'gcd']params: [#Arguments [#Name 'b'][#Infix left: [#Name 'a']name: [#Name '%']right: [#Name 'b']]]]]]]
# gcd(a,b)をresultとする
result = gcd(a, b)
# resultを出力する
print(result)