# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x,y = map(int,input().split())
# 真の間、繰り返す
while True :
  # xがyより小さいとき、
  if x<y :
    # xとyを入れ替える
    x, y = y, x
  # xをyで割った余りをamariとする
  amari = x%y
  # amariが0のとき、
  if amari==0 :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#MultiAssignment left: [# [#Name 'x'][#Name 'y']]right: [#Tuple [#Name 'y'][#Name 'amari']]]]]
# yを出力する
print(y)