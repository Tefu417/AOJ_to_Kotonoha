[#FromDecl name: [#ModuleName 'math']names: [# [#Name 'gcd']]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にnとmとする
n,m  = map(int,input().split())
# gcd(n,m)を出力する
print(gcd(n,m))