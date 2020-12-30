# 関数gdcを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def gdc (a,b) :[#Document [# 'print("%d, %d"%(a,b))']]
  # aとbの最小値が0のとき、
  if min(a,b) == 0 :
    # aを関数出力とする
    return a
  # ()
  else :[#Else [#Block [#Return expr: [#ApplyExpr name: [#Name 'gdc']params: [#Arguments [#ApplyExpr name: [#Name 'min']params: [#Arguments [#Name 'a'][#Name 'b']]][#Infix left: [#ApplyExpr name: [#Name 'max']params: [#Arguments [#Name 'a'][#Name 'b']]]name: [#Name '%']right: [#ApplyExpr name: [#Name 'min']params: [#Arguments [#Name 'a'][#Name 'b']]]]]]]]]
# {{入力された文字列を" "で分割した列}}の各要素をsとし、sの整数値の列をaとする
a = [int(s) for s in input().split(" ")]
# gdc(aの最初値,a(1))を出力する
print(gdc(a[0],a[1]))