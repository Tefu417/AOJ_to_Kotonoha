# {{入力された文字列を空白で分割した列}}の各要素をxとし、xの整数値の列を展開し順にxとyとする
x, y  = [int(x) for x in input().split()]
# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def gcd (x,y) :
  # yが0のとき、
  if y == 0 :
    # xを出力する
    print(x)
  # ()
  else :[#Else [#Block [#If cond: [#Infix left: [#Name 'x']name: [#Name '>=']right: [#Name 'y']]then: [#Block [#Expression [#ApplyExpr name: [#Name 'gcd']params: [#Arguments [#Name 'y'][#Infix left: [#Name 'x']name: [#Name '%']right: [#Name 'y']]]]]]else: [#Else [#Block [#Expression [#ApplyExpr name: [#Name 'gcd']params: [#Arguments [#Name 'x'][#Infix left: [#Name 'y']name: [#Name '%']right: [#Name 'x']]]]]]]]]]
# gcd(x,y)
gcd(x,y)