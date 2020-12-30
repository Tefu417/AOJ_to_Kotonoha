# fractionsモジュールを用いる
import fractions
# 入力された文字列の整数値をNとする
N = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをdataとする
data = list(map(int,input().split()))
# dataの最初値をxとする
x = data[0]
# '1からN未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1, N) :
  # xにdata(i)を掛けた値をfractions.gcd(x, data[i])で割った商をxとする
  x = x * data[i] // fractions.gcd(x, data[i])
# xを出力する
print(x)