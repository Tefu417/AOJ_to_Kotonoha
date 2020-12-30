# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをnumとする
num = list(map(int,input().split()))
# numの最初値がnum(1)より大きいとき、
if num[0]>num[1] :
  # numの最初値をxとする
  x = num[0]
  # num(1)をyとする
  y = num[1]
# ('numの最初値がnum(1)より小さい',)
elif num[0]<num[1] :
  # num(1)をxとする
  x = num[1]
  # numの最初値をyとする
  y = num[0]
# ()
else :[#Else [#Block [#VarDecl name: [#Name 'x']expr: [#IndexExpr recv: [#Name 'num']index: [#Int '1']]][#VarDecl name: [#Name 'y']expr: [#IndexExpr recv: [#Name 'num']index: [#Int '0']]][#VarDecl name: [#Name 'b']expr: [#IndexExpr recv: [#Name 'num']index: [#Int '1']]]]]
# xをyで割った余りをaとする
a = x%y
# aが0と等しくない間、繰り返す
while a!=0 :
  # aをbとする
  b = a
  # yをaで割った余りをaとする
  a = y%a
  # bをyとする
  y = b
# bを出力する
print(b)