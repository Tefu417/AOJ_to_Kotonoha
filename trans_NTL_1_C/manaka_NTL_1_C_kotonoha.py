# mathモジュールを用いる
import math
# 入力された文字列
input()
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをLとする
L = list(map(int, input().split()))
# {{'0からLの長さ未満までの数列}}の各要素をxとし、空列の列をmとする
m = [ [] for x in range(len(L))]
# '0からLの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(L)) :
  # L(i)をnとする
  n = L[i]
  # nをkとする
  k = n
  # '2からmath.sqrt(n)の整数値に1を加えた値未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(2, int(math.sqrt(n))+1) :
    # jがkより大きいとき、
    if j > k :
      # 繰り返すのを中断する
      break
    # kをjで割った余りが0の間、繰り返す
    while k % j ==0 :
      # m[i].append(j)
      m[i].append(j)
      # kをjで割った商をkとする
      k = k // j
      # kが1のとき、
      if k == 1 :
        # 繰り返すのを中断する
        break
  # kが1と等しくないとき、
  if k != 1 :
    # m[i].append(k)
    m[i].append(k)
# 集合をsとする
s = set()
# mの各要素を順にiとして、繰り返す
for i  in m :
  # ([[#Name 's'], [#ApplyExpr name: [#Name 'set']params: [#Arguments [#Name 'i']]]],)
  [[#Name 's'], [#ApplyExpr name: [#Name 'set']params: [#Arguments [#Name 'i']]]]
# 1をlcmとする
lcm = 1
# sの各要素を順にiとして、繰り返す
for i  in s :
  # ([[#Name 'lcm'], [#Infix left: [#Name 'i']name: [#Name '**']right: [#ApplyExpr name: [#Name 'max']params: [#Arguments [#List [#ForExpr append: [#MethodExpr recv: [#IndexExpr recv: [#Name 'm']index: [#Name 'x']]name: [#Name 'count']params: [#Arguments [#Name 'i']]]each: [# [#Name 'x']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'L']]]]]]]]]]],)
  [[#Name 'lcm'], [#Infix left: [#Name 'i']name: [#Name '**']right: [#ApplyExpr name: [#Name 'max']params: [#Arguments [#List [#ForExpr append: [#MethodExpr recv: [#IndexExpr recv: [#Name 'm']index: [#Name 'x']]name: [#Name 'count']params: [#Arguments [#Name 'i']]]each: [# [#Name 'x']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'L']]]]]]]]]]]
# lcmを出力する
print(lcm)