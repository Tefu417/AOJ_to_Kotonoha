# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x,y = map(int,input().split())
# yがxより大きいとき、
if y>x :
  # xとyを入れ替える
  x, y = y, x
# 真の間、繰り返す
while True :
  # xをyで割った余りをzとする
  z = x%y
  # zが0のとき、
  if z==0 :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'x']expr: [#Name 'y']][#VarDecl name: [#Name 'y']expr: [#Name 'z']]]]
# yを出力する
print(y)