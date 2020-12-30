# fractionsモジュールを用いる
import fractions
# 入力された文字列の整数値をnとする
n = int(input())
# 入力された文字列を空白で分割した列をaとする
a = input().split()
# 'map(整数,a)のリストをlとする
l = list(map(int,a))
# lの最初値をansとする
ans = l[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1,n) :
  # ansにl(i)を掛けた値をfractions.gcd(ans,l[i])で割った商をansとする
  ans = ans * l[i] // fractions.gcd(ans,l[i])
# ansを出力する
print(ans)