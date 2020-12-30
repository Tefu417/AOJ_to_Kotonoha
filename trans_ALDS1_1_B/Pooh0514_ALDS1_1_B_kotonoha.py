[#Document [# 'coding: utf-8']][#Document [# 'Your code here!']]
# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def gcd (x, y) :
  # xをyで割った余りが0のとき、
  if x % y == 0 :
    # yを関数出力とする
    return y
  # ()
  else :[#Else [#Block [#Return expr: [#ApplyExpr name: [#Name 'gcd']params: [#Arguments [#Name 'y'][#Infix left: [#Name 'x']name: [#Name '%']right: [#Name 'y']]]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x, y  = map(int, input().split())
# xがyより小さいとき、
if x < y :
  # xとyを入れ替える
  x, y = y, x
# gcd(x,y)を出力する
print(gcd(x, y))