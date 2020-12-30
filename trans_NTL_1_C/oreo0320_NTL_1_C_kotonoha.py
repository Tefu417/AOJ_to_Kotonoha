# mathモジュールを用いる
import math
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをlstとする
lst = list(map(int,input().split()))
# lstの最初値をansとする
ans = lst[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1,n) :
  # ansにlst(i)を掛けた値をmath.gcd(ans,lst[i])で割った商をansとする
  ans = ans*lst[i]//math.gcd(ans,lst[i])
# ansを出力する
print(ans)