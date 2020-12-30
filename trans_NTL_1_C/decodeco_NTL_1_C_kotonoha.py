# fractionsモジュールを用いる
import fractions
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをlとする
l = list(map(int,input().split()))
# lの最初値をmとする
m = l[0]
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # mにl(i)を掛けた値をfractions.gcd(m,l[i])で割った商をmとする
  m = m*l[i]//fractions.gcd(m,l[i])
# mを出力する
print(m)