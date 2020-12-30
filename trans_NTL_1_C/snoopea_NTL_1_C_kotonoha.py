# fractionsモジュールを用いる
import fractions
# 入力された文字列の整数値をnとする
n = int(input())
# '{{入力された文字列を空白で分割した列}}の各要素をzとし、zの整数値の列のリストをaとする
a = list(int(z) for z in input().split())
# aの最初値をAとする
A = a[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1,n) :
  # Aにa(i)を掛けた値をfra.gcd(A,a[i])で割った商をAとする
  A = A*a[i]//fra.gcd(A,a[i])
# Aを出力する
print(A)