# mathモジュールを用いる
import math
# 入力された文字列の整数値をiとする
i = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをlineとする
line = list(map(int,input().split()))
# lineの最初値をnとする
n = line[0]
# '1からi未満までの数列の各要素を順にlとして、繰り返す
for l  in range(1,i) :
  # {{nにline(l)を掛けた値}}をmath.gcd(n,line[l])で割った値の整数値をnとする
  n = int(n * line[l] / math.gcd(n,line[l]))
# nを出力する
print(n)