[#FromDecl name: [#ModuleName 'math']names: [# [#Name 'gcd']]]
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# aの最初値をbとする
b = a[0]
# aの先頭を除いた部分の各要素を順にiとして、繰り返す
for i  in a[1:] :
  # {{bにiを掛けた値}}をgcd(b,i)で割った値の整数値をbとする
  b = int(b*i/gcd(b, i))
# bを出力する
print(b)