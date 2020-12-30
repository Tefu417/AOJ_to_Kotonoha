# 入力された文字列をlineとする
line = input()
# ""をnewとする
new = ""
# '0からlineの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(line)) :
  # line(i)の全てが英小文字のとき、
  if line[i].islower() :
    # ([[#Name 'new'], [#MethodExpr recv: [#IndexExpr recv: [#Name 'line']index: [#Name 'i']]name: [#Name 'upper']params: [#Arguments '']]],)
    [[#Name 'new'], [#MethodExpr recv: [#IndexExpr recv: [#Name 'line']index: [#Name 'i']]name: [#Name 'upper']params: [#Arguments '']]]
  # ('line(i)の全てが英大文字の',)
  elif line[i].isupper() :
    # ([[#Name 'new'], [#MethodExpr recv: [#IndexExpr recv: [#Name 'line']index: [#Name 'i']]name: [#Name 'lower']params: [#Arguments '']]],)
    [[#Name 'new'], [#MethodExpr recv: [#IndexExpr recv: [#Name 'line']index: [#Name 'i']]name: [#Name 'lower']params: [#Arguments '']]]
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 'new']name: [# '+=']right: [#IndexExpr recv: [#Name 'line']index: [#Name 'i']]]]]
# newを出力する
print(new)