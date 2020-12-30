[#FromDecl name: [#ModuleName 'math']names: [# [#Name 'gcd']]]
# 1をaとする
a = 1
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをlとする
l = list(map(int,input().split()))
# lの各要素を順にiとして、繰り返す
for i  in l :
  # aにiを掛けた値をgcd(a,i)で割った商をaとする
  a = a*i//gcd(a,i)
# aを出力する
print(a)