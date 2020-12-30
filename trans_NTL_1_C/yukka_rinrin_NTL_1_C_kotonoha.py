# fractionsモジュールを用いる
import fractions
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをmとする
m = list(map(int,input().split()))
# mの最初値をansとする
ans = m[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1,n) :
  # ansにm(i)を掛けた値をfractions.gcd(ans,m[i])で割った商をansとする
  ans = ans*m[i]//fractions.gcd(ans,m[i])
# ansを出力する
print(ans)