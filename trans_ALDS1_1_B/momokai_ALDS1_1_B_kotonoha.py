[#Document [# 'coding: utf-8']][#Document [# 'Your code here!']]
# mathモジュールを用いる
import math
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int,input().split())
# math.gcd(a,b)を出力する
print(math.gcd(a,b))