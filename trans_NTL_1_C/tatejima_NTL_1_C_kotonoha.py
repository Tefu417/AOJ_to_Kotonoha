# fractionsモジュールを用いる
import fractions
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをxとする
x = list(map(int, input().split()))   
# xの最初値をyとする
y = x[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1,n) :
  # yにx(i)を掛けた値をfractions.gcd(y, x[i])で割った商をyとする
  y = y * x[i] // fractions.gcd(y, x[i])
# yを出力する
print(y)