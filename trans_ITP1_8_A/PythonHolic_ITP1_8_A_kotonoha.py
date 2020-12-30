# 入力された文字列をsとする
s = input()
# ''をtとする
t = ''
# sの各要素を順にwとして、繰り返す
for w  in s :
  # wの全てが英大文字のとき、
  if w.isupper() :
    # ([[#Name 't'], [#MethodExpr recv: [#Name 'w']name: [#Name 'lower']params: [#Arguments '']]],)
    [[#Name 't'], [#MethodExpr recv: [#Name 'w']name: [#Name 'lower']params: [#Arguments '']]]
  # ('wの全てが英小文字の',)
  elif w.islower() :
    # ([[#Name 't'], [#MethodExpr recv: [#Name 'w']name: [#Name 'upper']params: [#Arguments '']]],)
    [[#Name 't'], [#MethodExpr recv: [#Name 'w']name: [#Name 'upper']params: [#Arguments '']]]
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 't']name: [# '+=']right: [#Name 'w']]]]
# tを出力する
print (t)