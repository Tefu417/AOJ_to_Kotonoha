[#Document [# 'coding: utf-8']][#Document [# '76']]
# fractionsモジュールを用いる
import fractions
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# aの最初値をansとする
ans = a[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1,n) :
  # ansにa(i)を掛けた値をfractions.gcd(ans,a[i])で割った商をansとする
  ans = ans*a[i] // fractions.gcd(ans,a[i])
# ansを出力する
print(ans)