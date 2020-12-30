# fractionsモジュールを用いる
import fractions
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int, input().split()))
# aの最初値をbとする
b = a[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1, n) :
  # bにa(i)を掛けた値をfractions.gcd(b, a[i])で割った商をbとする
  b = b*a[i]//fractions.gcd(b, a[i])
# bを出力する
print(b)