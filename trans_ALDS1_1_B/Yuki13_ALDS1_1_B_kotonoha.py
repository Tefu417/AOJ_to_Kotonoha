# mathモジュールを用いる
import math
# 入力された文字列を空白で分割した列の各要素をxとし、xの整数値の列をxとyとする
x,y  = (int(x) for x in input().split())
# math.gcd(x,y)を出力する
print(math.gcd(x,y))