# fractionsモジュールを用いる
import fractions
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをlとする
l = list(map(int,input().split()))
# lの最初値をaとする
a = l[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1,n) :
  # aにl(i)を掛けた値をfractions.gcd(a,l[i])で割った商をaとする
  a = a*l[i]//fractions.gcd(a,l[i])
# aを出力する
print(a)