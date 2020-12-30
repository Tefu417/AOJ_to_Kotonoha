# mathモジュールを用いる
import math
# 入力された文字列の整数値をlとする
l = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int, input().split()))
# 空辞書をdictとする
dict = {}
# aの各要素を順にnとして、繰り返す
for n  in a :
  # 空列をansとする
  ans = []
  # 2をiとする
  i = 2
  # math.sqrt(n)をkとする
  k = math.sqrt(n)
  # 空辞書をdicとする
  dic = {}
  # iがk以下の間、繰り返す
  while i <= k :
    # nをiで割った余りが0のとき、
    if n%i == 0 :
      # nをiで割った商をnとする
      n = n//i
      # ans.append(i)
      ans.append(i)
      # ([[#Name 'i'], [#Int '1']],)
      [[#Name 'i'], [#Int '1']]
      # nが1のとき、
      if n == 1 :
        # 繰り返すのを中断する
        break
    # ([[#Name 'i'], [#Int '1']],)
    [[#Name 'i'], [#Int '1']]
  # ansの長さが0、またはnが1と等しくないとき、
  if len(ans) == 0 or n != 1 :
    # ans.append(n)
    ans.append(n)
  # ansの各要素を順にiとして、繰り返す
  for i  in ans :
    # iがdicに含まれるとき、
    if i in dic :
      # ([[#IndexExpr recv: [#Name 'dic']index: [#Name 'i']], [#Int '1']],)
      [[#IndexExpr recv: [#Name 'dic']index: [#Name 'i']], [#Int '1']]
    # ()
    else :[#Else [#Block [#Assignment left: [#IndexExpr recv: [#Name 'dic']index: [#Name 'i']]right: [#Int '1']]]]
  # dic.keys()の各要素を順にiとして、繰り返す
  for i  in dic.keys() :
    # iが辞書に含まれるとき、
    if i in dict :
      # 辞書(i)とdic(i)の最大値をdict[i] にする
      dict[i]  = max(dict[i], dic[i])
    # ()
    else :[#Else [#Block [#Assignment left: [#IndexExpr recv: [#Name 'dict']index: [#Name 'i']]right: [#IndexExpr recv: [#Name 'dic']index: [#Name 'i']]]]]
# 1をsumとする
sum = 1
# dict.items()の各要素を順にxとyとして、繰り返す
for x,y  in dict.items() :
  # ([[#Name 'sum'], [#Infix left: [#Name 'x']name: [#Name '**']right: [#Name 'y']]],)
  [[#Name 'sum'], [#Infix left: [#Name 'x']name: [#Name '**']right: [#Name 'y']]]
# sumを出力する
print(sum)