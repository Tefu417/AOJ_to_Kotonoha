# 入力された文字列をmとする
m = input()
# ''をkとする
k = ''
# mの各要素を順にiとして、繰り返す
for i  in m :
  # iが' '、またはiが'.'のとき、
  if i == ' ' or i == '.' :
    # kにiを加えた値をkとする
    k = k + i
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'k']expr: [#Infix left: [#Name 'k']name: [#Name '+']right: [#ApplyExpr name: [#Name 'chr']params: [#Arguments [#Infix left: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#Name 'i']]]name: [#Name '-']right: [#Int '32']]]]]]]]
# kを出力する
print(k)