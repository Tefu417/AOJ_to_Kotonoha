# functoolsモジュールを用いる
import functools
# mathモジュールを用いる
import math
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を" "で分割した列}})のリストをaとする
a = list(map(int,input().split(" ")))
# functools.reduce(lambda x, y: x*y//math.gcd(x,y), a)を出力する
print(functools.reduce(lambda x, y: x*y//math.gcd(x,y), a))