# mathモジュールを用いる
import math
# 入力された文字列の整数値をnとする
n = int(input())
# {{入力された文字列を空白で分割した列}}の各要素をaとし、aの整数値の列をAとする
A = [int(a) for a in input().split()]
# Aの最初値をansとする
ans = A[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1, n)  :
  # ansにA(i)を掛けた値をmath.gcd(ans, A[i])で割った商をansとする
  ans = ans * A[i] // math.gcd(ans, A[i])
# ansを出力する
print(ans)