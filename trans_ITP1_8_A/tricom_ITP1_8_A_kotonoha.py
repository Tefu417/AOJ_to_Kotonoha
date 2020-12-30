# 入力された文字列をsとする
s = input()
# ""をs2とする
s2 = ""
# sの各要素を順にiとして、繰り返す
for i  in s :
  # iの全てが英大文字のとき、
  if i.isupper() :
    # ([[#Name 's2'], [#MethodExpr recv: [#Name 'i']name: [#Name 'lower']params: [#Arguments '']]],)
    [[#Name 's2'], [#MethodExpr recv: [#Name 'i']name: [#Name 'lower']params: [#Arguments '']]]
  # ('iの全てが英小文字の',)
  elif i.islower() :
    # ([[#Name 's2'], [#MethodExpr recv: [#Name 'i']name: [#Name 'upper']params: [#Arguments '']]],)
    [[#Name 's2'], [#MethodExpr recv: [#Name 'i']name: [#Name 'upper']params: [#Arguments '']]]
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 's2']name: [# '+=']right: [#Name 'i']]]]
# s2を出力する
print(s2)