# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def gcd (x, y) :
  # yが0のとき、
  if y == 0 :
    # xを関数出力とする
    return x
  # ()
  else :[#Else [#Block [#Return expr: [#ApplyExpr name: [#Name 'gcd']params: [#Arguments [#Name 'y'][#Infix left: [#Name 'x']name: [#Name '%']right: [#Name 'y']]]]]]]
# map(整数,{{入力された文字列の両端から空白改行を取り除いた文字列}}を空白で分割した列)を展開し順にxとyとする
x, y  = map(int, input().strip().split())
# gcd(x,y)を出力する
print(gcd(x, y))