# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int, input().split()))
# 空列をlとする
l = []
# 空列をansとする
ans = []
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # 空列をpとする
  p = []
  # a(i)が1のとき、
  if a[i] == 1 :
    # p.append(1)
    p.append(1)
  # ()
  else :[#Else [#Block [#For each: [# [#Name 'j']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '1'][#Infix left: [#Infix left: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#Infix left: [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]name: [#Name '**']right: [#Double '0.5']]]]name: [#Name '//']right: [#Int '2']]name: [#Name '+']right: [#Int '1']]]]body: [#Block [#While cond: [#Infix left: [#Infix left: [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]name: [#Name '%']right: [#Int '2']]name: [#Name '==']right: [#Int '0']]body: [#Block [#Expression [#MethodExpr recv: [#Name 'p']name: [#Name 'append']params: [#Arguments [#Int '2']]]][#Assignment left: [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]right: [#Infix left: [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]name: [#Name '//']right: [#Int '2']]]]][#While cond: [#Infix left: [#Infix left: [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]name: [#Name '%']right: [#Tuple [#Infix left: [#Infix left: [#Int '2']name: [#Name '*']right: [#Name 'j']]name: [#Name '+']right: [#Int '1']]]]name: [#Name '==']right: [#Int '0']]body: [#Block [#Expression [#MethodExpr recv: [#Name 'p']name: [#Name 'append']params: [#Arguments [#Infix left: [#Infix left: [#Int '2']name: [#Name '*']right: [#Name 'j']]name: [#Name '+']right: [#Int '1']]]]][#Assignment left: [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]right: [#Infix left: [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]name: [#Name '//']right: [#Tuple [#Infix left: [#Infix left: [#Int '2']name: [#Name '*']right: [#Name 'j']]name: [#Name '+']right: [#Int '1']]]]]]]]]]]
  # a(i)が1と等しくないとき、
  if a[i] != 1 :
    # p.append(a[i])
    p.append(a[i])
  # l.append(p)
  l.append(p)
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # '0からl(i)の長さ未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(len(l[i])) :
    # not in(l(i)(j),ans)のとき、
    if l[i][j] not in ans :
      # ans.append(l[i][j])
      ans.append(l[i][j])
    # ()
    else :[#Else [#Block [#VarDecl name: [#Name 'm']expr: [#Infix left: [#MethodExpr recv: [#IndexExpr recv: [#Name 'l']index: [#Name 'i']]name: [#Name 'count']params: [#Arguments [#IndexExpr recv: [#IndexExpr recv: [#Name 'l']index: [#Name 'i']]index: [#Name 'j']]]]name: [#Name '-']right: [#MethodExpr recv: [#Name 'ans']name: [#Name 'count']params: [#Arguments [#IndexExpr recv: [#IndexExpr recv: [#Name 'l']index: [#Name 'i']]index: [#Name 'j']]]]]][#If cond: [#Infix left: [#Name 'm']name: [#Name '>']right: [#Int '0']]then: [#Block [#For each: [# [#Name 'k']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'm']]]body: [#Block [#Expression [#MethodExpr recv: [#Name 'ans']name: [#Name 'append']params: [#Arguments [#IndexExpr recv: [#IndexExpr recv: [#Name 'l']index: [#Name 'i']]index: [#Name 'j']]]]]]]]]]]
# 1をxとする
x = 1
# ansの各要素を順にiとして、繰り返す
for i  in ans :
  # ([[#Name 'x'], [#Name 'i']],)
  [[#Name 'x'], [#Name 'i']]
# xを出力する
print(x)