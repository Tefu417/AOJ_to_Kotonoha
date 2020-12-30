[#FromDecl name: [#ModuleName 'math']names: [# [#Name 'gcd']]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x, y  = map(int,input().split())
# gcd(x,y)を出力する
print(gcd(x,y))