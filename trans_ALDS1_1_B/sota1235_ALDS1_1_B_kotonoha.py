# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# aがbより大きいとき、
if a > b :
  # aとbを入れ替える
  a, b = b, a
# 真の間、繰り返す
while True :
  # bをaで割った余りが0のとき、
  if b % a == 0 :
    # aを出力する
    print(a)
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'b']expr: [#Infix left: [#Name 'b']name: [#Name '%']right: [#Name 'a']]][#If cond: [#Infix left: [#Name 'a']name: [#Name '>']right: [#Name 'b']]then: [#Block [#MultiAssignment left: [# [#Name 'a'][#Name 'b']]right: [#Tuple [#Name 'b'][#Name 'a']]]]]]]