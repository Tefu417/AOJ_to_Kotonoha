# mathモジュールを用いる
import math
## 2の数をint型にしてリストのにインプットする
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをnum_listとする
num_list = list(map(int,input().split())) 
## 2つの数の最大公約数をとる
# math.gcd(num_list[0],num_list[1])を出力する
print(math.gcd(num_list[0],num_list[1])) 