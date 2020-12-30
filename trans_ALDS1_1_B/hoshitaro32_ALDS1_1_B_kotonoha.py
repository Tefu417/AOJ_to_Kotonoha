[#FromDecl name: [#ModuleName 'fractions']names: [# [#Name 'gcd']]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a,b  = map(int,input().split())
# gcd(a,b)を出力する
print(gcd(a,b))