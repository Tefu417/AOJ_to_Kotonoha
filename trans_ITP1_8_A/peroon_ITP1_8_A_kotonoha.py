[#Document [# '-*- coding: utf-8 -*-']]
# sysモジュールを用いる
import sys
# osモジュールを用いる
import os
# 入力された文字列の両端から空白改行を取り除いた文字列をsとする
s = input().strip()
# sの各要素を順にcとして、繰り返す
for c  in s :
  # cの全てが英小文字のとき、
  if c.islower() :
    # cを英大文字に変換した文字列と((end, ''))からなる辞書を出力する
    print(c.upper(), end='')
  # ('cの全てが英大文字の',)
  elif c.isupper() :
    # cを英小文字に変換した文字列と((end, ''))からなる辞書を出力する
    print(c.lower(), end='')
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'c'][#Data [#KeyValue name: [#Name 'end']value: [#QString "''"]]]]]]]]
# 空行を出力する
print()