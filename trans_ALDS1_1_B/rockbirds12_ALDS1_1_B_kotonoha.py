# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをソートした列をxとする
x = sorted(list(map(int, input().split())))
# 真の間、繰り返す
while True :
  # x(1)をx(0)で割った余りが0のとき、
  if x[1] % x[0] == 0 :
    # xの最初値を出力する
    print(x[0])
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'tmp']expr: [#Infix left: [#IndexExpr recv: [#Name 'x']index: [#Int '1']]name: [#Name '%']right: [#IndexExpr recv: [#Name 'x']index: [#Int '0']]]][#Assignment left: [#IndexExpr recv: [#Name 'x']index: [#Int '1']]right: [#IndexExpr recv: [#Name 'x']index: [#Int '0']]][#Assignment left: [#IndexExpr recv: [#Name 'x']index: [#Int '0']]right: [#Name 'tmp']]]]