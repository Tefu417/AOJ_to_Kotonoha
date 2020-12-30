[#Document [# '! python3']][#Document [# 'toggling_cases.py']]
# 入力された文字列をxとする
x = input()
# ''をrstとする
rst = ''
# xの各要素を順にcとして、繰り返す
for c  in x :
  # cの全てが英大文字のとき、
  if c.isupper() :
    # ([[#Name 'rst'], [#MethodExpr recv: [#Name 'c']name: [#Name 'lower']params: [#Arguments '']]],)
    [[#Name 'rst'], [#MethodExpr recv: [#Name 'c']name: [#Name 'lower']params: [#Arguments '']]]
  # ('cの全てが英小文字の',)
  elif c.islower() :
    # ([[#Name 'rst'], [#MethodExpr recv: [#Name 'c']name: [#Name 'upper']params: [#Arguments '']]],)
    [[#Name 'rst'], [#MethodExpr recv: [#Name 'c']name: [#Name 'upper']params: [#Arguments '']]]
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 'rst']name: [# '+=']right: [#Name 'c']]]]
# rstを出力する
print(rst)