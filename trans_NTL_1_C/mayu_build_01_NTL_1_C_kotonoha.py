[#FromDecl name: [#ModuleName 'math']names: [# [#Name 'gcd']]]
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int, input().split()))
# aの最初値をxとする
x = a[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1,n) :
  # ({{xにa(i)を掛けた値}}をgcd(x,a(i))で割った商)の組をxとする
  x = (x*a[i]//gcd(x,a[i]))
# xを出力する
print(x)