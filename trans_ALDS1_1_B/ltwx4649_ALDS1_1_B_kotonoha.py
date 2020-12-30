# fractionsモジュールを用いる
import fractions
# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x,y = map(int,input().split())
# fractions.gcd(x,y)をAとする
A = fractions.gcd(x,y)
# Aを出力する
print(A)