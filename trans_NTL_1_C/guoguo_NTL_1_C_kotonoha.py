[#Document [# 'coding: utf-8']][#Document [# 'Your code here!']]
# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def gcd (x, y) :
  # xがyより小さいとき、
  if x < y :
    # xとyを入れ替える
    x, y = y, x
  # xをyで割った余りが0のとき、
  if x % y == 0 :
    # yを関数出力とする
    return y
  # ()
  else :[#Else [#Block [#Return expr: [#ApplyExpr name: [#Name 'gcd']params: [#Arguments [#Name 'y'][#Infix left: [#Name 'x']name: [#Name '%']right: [#Name 'y']]]]]]]
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをAとする
A = list(map(int, input().split()))
# Aの最初値をlとする
l = A[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1, n) :
  # lにA(i)を掛けた値をgcd(l,A(i))で割った値をlとする
  l = l * A[i] / gcd(l, A[i])
# lの整数値を出力する
print(int(l))