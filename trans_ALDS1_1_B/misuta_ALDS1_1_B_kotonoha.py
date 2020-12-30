# mathモジュールを用いる
import math
# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x, y  = map(int, input().split())
# math.gcd(x, y)を出力する
print(math.gcd(x, y))