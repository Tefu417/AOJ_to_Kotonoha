# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def gcd (a,b) :
  # aがbより大きいとき、
  if a>b :
    # aをxとする
    x = a
    # bをyとする
    y = b
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'x']expr: [#Name 'b']][#VarDecl name: [#Name 'y']expr: [#Name 'a']]]]
  # yが0のとき、
  if y==0 :
    # xを関数出力とする
    return x
  # ()
  else :[#Else [#Block [#Return expr: [#ApplyExpr name: [#Name 'gcd']params: [#Arguments [#Name 'y'][#Infix left: [#Name 'x']name: [#Name '%']right: [#Name 'y']]]]]]]
# {{入力された文字列を" "で分割した列}}の各要素をiとし、iの整数値の列を展開し順にpとqとする
p,q = [int(i) for i in input().split(" ")]
# gcd(p,q)を出力する
print(gcd(p,q))