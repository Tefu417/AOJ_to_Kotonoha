
# "Hello World"を出力する
print("Hello World")
# 入力された文字列の整数値をxとする
x = int(input())
# xの3乗を出力する
print(x ** 3)
# 入力された文字列の整数値をWとする
W = int(input())
# Wに32を掛けた値を出力する
print(W * 32)
# 入力された文字列の整数値をFとする
F = int(input())
# ({{Fから30を引いた値}})の組を2で割った商を出力する
print((F - 30) // 2)
# map(整数,入力された文字列を空白で分割した列)を展開し順にp、m、cとする
p, m, c  = map(int, input().split())
# {{pにmを加えた値}}にcを加えた値を出力する
print(p + m + c)
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# aにbを掛けた値をsとする
s = a * b
# aに2を掛けた値にbに2を掛けた値を加えた値をlとする
l = a * 2 + b * 2
# sとlを出力する
print(s, l)
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# aがbのとき、
if a == b  :
  # "a == b"を出力する
  print("a == b")
# ('aがbより小さい',)
elif a < b  :
  # "a < b"を出力する
  print("a < b")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"a > b"']]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a, b, c  = map(int, input().split())
# aがbより小さく、かつbがcより小さいとき、
if a < b and b < c  :
  # "Yes"を出力する
  print("Yes")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"No"']]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# ({{aにbを加えた値}})の組を2で割った商を出力する
print((a + b) // 2)
# map(整数,入力された文字列を空白で分割した列)を展開し順にx1とx2とする
x1, x2  = map(int, input().split())
# {{x1からx2を引いた値}}の絶対値を出力する
print(abs(x1 - x2))
# 入力された文字列をBとする
B = input()
# ("1 1 0"と"0 0 1")からなる列をOとする
O = ["1 1 0", "0 0 1"]
# BがOに含まれるとき、
if B in O  :
  # "Open"を出力する
  print("Open")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"Close"']]]]]]
# 入力された文字列の整数値をSとする
S = int(input())
# Sを3600で割った商をhとする
h = S // 3600
# ({{Sから{{hに3600を掛けた値}}を引いた値}})の組を60で割った商をmとする
m = (S - h * 3600) // 60
# Sから({{{{hに3600を掛けた値}}に{{mに60を掛けた値}}を加えた値}})の組を引いた値をsとする
s = S - (h * 3600 + m * 60)
# h、":"、m、":"、s、((sep, ""))からなる辞書を出力する
print(h, ":", m, ":", s, sep = "")
Syntax Error ((unknown source):7:18+88)
print(f"{d} {r} {f:.6f}")
                  ^      
Syntax Error ((unknown source):8:10+84)
print(f"{s:.6f} {l:.6f}")
          ^              
Syntax Error ((unknown source):5:10+66)
print(f"{S:.6f}")
          ^      
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a, b, c  = map(int, input().split())
# aがbより小さいとき、
if a < b  :
  # bがcより小さいとき、
  if b < c  :
    # a、b、cを出力する
    print(a, b, c)
  # ('aがcより小さい',)
  elif a < c  :
    # a、c、bを出力する
    print(a, c, b)
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'c'][#Name 'a'][#Name 'b']]]]]]
# ('bがaより小さい',)
elif b < a  :
  # aがcより小さいとき、
  if a < c  :
    # b、a、cを出力する
    print(b, a, c)
  # ('bがcより小さい',)
  elif b < c  :
    # b、c、aを出力する
    print(b, c, a)
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'c'][#Name 'b'][#Name 'a']]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にW、H、x、y、rとする
W, H, x, y, r  = map(int, input().split())
# {{xからrを引いた値}}が0以上、かつ{{yからrを引いた値}}が0以上のとき、
if x - r >= 0 and y - r >= 0  :
  # {{xにrを加えた値}}がW以下、かつ{{yにrを加えた値}}がH以下のとき、
  if x + r <= W and y + r <= H  :
    # "Yes"を出力する
    print("Yes")
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"No"']]]]]]
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"No"']]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にe1、e2、e3、e4とする
e1, e2, e3, e4  = map(int, input().split())
# (e1、e2、e3、e4)からなる列をEとする
E = [e1, e2, e3, e4]
# Eの集合をeとする
e = set(E)
# 'eのリストをe_listとする
e_list = list(e)
# eの長さが2のとき、
if len(e) == 2  :
  # E内のe_listの最初値の出現をカウントした整数が2のとき、
  if E.count(e_list[0]) == 2  :
    # "yes"を出力する
    print("yes")
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"no"']]]]]]
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"no"']]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にN、A、B、C、Dとする
N, A, B, C, D  = map(int, input().split())
# NをAで割った商をaとする
a = N // A
# NをCで割った商をcとする
c = N // C
# aにAを掛けた値がNより小さいとき、
if a * A < N  :
  # ([[#Name 'a'], [#Int '1']],)
  [[#Name 'a'], [#Int '1']]
# cにCを掛けた値がNより小さいとき、
if c * C < N  :
  # ([[#Name 'c'], [#Int '1']],)
  [[#Name 'c'], [#Int '1']]
# aにBを掛けた値をbとする
b = a * B
# cにDを掛けた値をdとする
d = c * D
# bがdより小さいとき、
if b < d  :
  # bを出力する
  print(b)
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'd']]]]]]
Syntax Error ((unknown source):16:-1+243)
else :
      
# '0から1000未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1000)  :
  # "Hello World"を出力する
  print("Hello World")
# ((1, 6000)、(2, 4000)、(3, 3000)、(4, 2000))からなる辞書をdicとする
dic = {1 : 6000, 2 : 4000, 3 : 3000, 4 : 2000}
# '0から4未満までの数列の各要素を順にiとして、繰り返す
for i  in range(4)  :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にtとnとする
  t, n  = map(int, input().split())
  # dic(t)にnを掛けた値を出力する
  print(dic[t] * n)
# '0から7未満までの数列の各要素を順にiとして、繰り返す
for i  in range(7)  :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
  a, b  = map(int, input().split())
  # aからbを引いた値を出力する
  print(a - b)
# '0から9未満までの数列の各要素を順にiとして、繰り返す
for i  in range(9)  :
  # map(str,入力された文字列を空白で分割した列)を展開し順にe、a、bとする
  e, a, b  = map(str, input().split())
  # aの整数値をaとする
  a = int(a)
  # bの整数値をbとする
  b = int(b)
  # e、aにbを加えた値、{{aに200を掛けた値}}に{{bに300を掛けた値}}を加えた値を出力する
  print(e, a + b, a * 200 + b * 300)
# 0をsとする
s = 0
# '0から10未満までの数列の各要素を順にiとして、繰り返す
for i  in range(10)  :
  # ([[#Name 's'], [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]],)
  [[#Name 's'], [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]]
# sを出力する
print(s)
# 0をiとする
i = 0
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をxとする
  x = int(input())
  # xが0のとき、
  if x == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 'i']name: [# '+=']right: [#Int '1']][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"Case "'][#Name 'i'][#QString '": "'][#Name 'x'][#Data [#KeyValue name: [#Name 'sep']value: [#QString '""']]]]]]]]
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
  x, y  = map(int, input().split())
  # xが0、かつyが0のとき、
  if x == 0 and y == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#If cond: [#Infix left: [#Name 'x']name: [#Name '<']right: [#Name 'y']]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'x'][#Name 'y']]]]]else: [#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'y'][#Name 'x']]]]]]]]]
# 入力された文字列の整数値をNとする
N = int(input())
# '0からN未満までの数列の各要素を順にiとして、繰り返す
for i  in range(N)  :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
  a, b, c  = map(int, input().split())
  # (a、b、c)からなる列をLとする
  L = [a, b, c]
  # L.pop(L.index(max(L)))をmとする
  m = L.pop(L.index(max(L)))
  # L(0)の2乗にL(1)の2乗を加えた値をsとする
  s = L[0] ** 2 + L[1] ** 2
  # mの2乗がsのとき、
  if m ** 2 == s  :
    # "YES"を出力する
    print("YES")
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"NO"']]]]]]
# 入力された文字列の整数値をnとする
n = int(input())
# 100000をsとする
s = 100000
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # ([[#Name 's'], [#Double '1.05']],)
  [[#Name 's'], [#Double '1.05']]
  # sを1000で割った余りをmとする
  m = s % 1000
  # mが0と等しくないとき、
  if m != 0  :
    # sからmを引いた値に1000を加えた値をsとする
    s = s - m + 1000
# sの整数値を出力する
print(int(s))
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # 0をsとする
  s = 0
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'm']expr: [#Infix left: [#Int '1000']name: [#Name '-']right: [#Name 'n']]][#If cond: [#Infix left: [#Name 'm']name: [#Name '>=']right: [#Int '500']]then: [#Block [#SelfAssignment left: [#Name 's']name: [# '+=']right: [#Int '1']][#SelfAssignment left: [#Name 'm']name: [# '-=']right: [#Int '500']]]][#While cond: [#Infix left: [#Name 'm']name: [#Name '>=']right: [#Int '100']]body: [#Block [#SelfAssignment left: [#Name 's']name: [# '+=']right: [#Int '1']][#SelfAssignment left: [#Name 'm']name: [# '-=']right: [#Int '100']]]][#While cond: [#Infix left: [#Name 'm']name: [#Name '>=']right: [#Int '50']]body: [#Block [#SelfAssignment left: [#Name 's']name: [# '+=']right: [#Int '1']][#SelfAssignment left: [#Name 'm']name: [# '-=']right: [#Int '50']]]][#While cond: [#Infix left: [#Name 'm']name: [#Name '>=']right: [#Int '10']]body: [#Block [#SelfAssignment left: [#Name 's']name: [# '+=']right: [#Int '1']][#SelfAssignment left: [#Name 'm']name: [# '-=']right: [#Int '10']]]][#While cond: [#Infix left: [#Name 'm']name: [#Name '>=']right: [#Int '5']]body: [#Block [#SelfAssignment left: [#Name 's']name: [# '+=']right: [#Int '1']][#SelfAssignment left: [#Name 'm']name: [# '-=']right: [#Int '5']]]][#SelfAssignment left: [#Name 's']name: [# '+=']right: [#Name 'm']]]]
  # sを出力する
  print(s)
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a, b, c  = map(int, input().split())
# 0をsとする
s = 0
# 'aからbに1を加えた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(a, b + 1)  :
  # cをiで割った余りが0のとき、
  if c % i == 0  :
    # ([[#Name 's'], [#Int '1']],)
    [[#Name 's'], [#Int '1']]
# sを出力する
print(s)
# '1から10未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1, 10)  :
  # '1から10未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(1, 10)  :
    # i、"x"、j、"="、iにjを掛けた値、((sep, ""))からなる辞書を出力する
    print(i, "x", j, "=", i * j, sep = "")
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にHとWとする
  H,W = map(int,input().split())
  # Hが0、かつWが0のとき、
  if H==0 and W==0 :
    # 繰り返すのを中断する
    break
  # '0からH未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(H) :
    # '0からW未満までの数列の各要素を順にjとして、繰り返す
    for j  in range(W) :
      # "#"と((end, ""))からなる辞書を出力する
      print("#",end="")
    # 空行を出力する
    print()
  # 空行を出力する
  print()
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にHとWとする
  H, W  = map(int, input().split())
  # Hが0のとき、
  if H == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'H']]]body: [#Block [#For each: [# [#Name 'j']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'W']]]body: [#Block [#If cond: [#Or left: [#Or left: [#Or left: [#Infix left: [#Name 'i']name: [#Name '==']right: [#Int '0']]right: [#Infix left: [#Name 'i']name: [#Name '==']right: [#Infix left: [#Name 'H']name: [#Name '-']right: [#Int '1']]]]right: [#Infix left: [#Name 'j']name: [#Name '==']right: [#Int '0']]]right: [#Infix left: [#Name 'j']name: [#Name '==']right: [#Infix left: [#Name 'W']name: [#Name '-']right: [#Int '1']]]]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"#"'][#Data [#KeyValue name: [#Name 'sep']value: [#QString '""']][#KeyValue name: [#Name 'end']value: [#QString '""']]]]]]]else: [#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"."'][#Data [#KeyValue name: [#Name 'sep']value: [#QString '""']][#KeyValue name: [#Name 'end']value: [#QString '""']]]]]]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments '']]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments '']]]]]
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にHとWとする
  H, W  = map(int, input().split())
  # Hが0のとき、
  if H == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'H']]]body: [#Block [#For each: [# [#Name 'j']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'W']]]body: [#Block [#If cond: [#Infix left: [#Infix left: [#Tuple [#Infix left: [#Name 'i']name: [#Name '+']right: [#Name 'j']]]name: [#Name '%']right: [#Int '2']]name: [#Name '==']right: [#Int '0']]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"#"'][#Data [#KeyValue name: [#Name 'sep']value: [#QString '""']][#KeyValue name: [#Name 'end']value: [#QString '""']]]]]]]else: [#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"."'][#Data [#KeyValue name: [#Name 'sep']value: [#QString '""']][#KeyValue name: [#Name 'end']value: [#QString '""']]]]]]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments '']]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments '']]]]]
# 真の間、繰り返す
while True :
  # map(str,入力された文字列を空白で分割した列)を展開し順にa、op、bとする
  a, op, b  = map(str, input().split())
  # aの整数値をaとする
  a = int(a)
  # bの整数値をbとする
  b = int(b)
  # opが"?"のとき、
  if op == "?"  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#If cond: [#Infix left: [#Name 'op']name: [#Name '==']right: [#QString '"+"']]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Infix left: [#Name 'a']name: [#Name '+']right: [#Name 'b']]]]]]elif: [# [#Elif cond: [#Infix left: [#Name 'op']name: [#Name '==']right: [#QString '"-"']]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Infix left: [#Name 'a']name: [#Name '-']right: [#Name 'b']]]]]]][#Elif cond: [#Infix left: [#Name 'op']name: [#Name '==']right: [#QString '"*"']]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Infix left: [#Name 'a']name: [#Name '*']right: [#Name 'b']]]]]]]]else: [#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Infix left: [#Name 'a']name: [#Name '//']right: [#Name 'b']]]]]]]]]]
# 入力された文字列の整数値をnとする
n = int(input())
# {{入力された文字列を空白で分割した列}}の各要素をaとし、aの整数値の列をAとする
A = [int(a) for a in input().split()]
# Aの最小値、Aの最大値、Aの総和を出力する
print(min(A), max(A), sum(A))
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # 空列をPとする
  P = []
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'n']]]body: [#Block [#Expression [#MethodExpr recv: [#Name 'P']name: [#Name 'append']params: [#Arguments [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]]]]]][#VarDecl name: [#Name 'Ps']expr: [#ApplyExpr name: [#Name 'sorted']params: [#Arguments [#Name 'P']]]][#Delete expr: [#IndexExpr recv: [#Name 'Ps']index: [#Int '0']]][#Delete expr: [#IndexExpr recv: [#Name 'Ps']index: [#Infix left: [#Name 'n']name: [#Name '-']right: [#Int '2']]]][#VarDecl name: [#Name 's']expr: [#ApplyExpr name: [#Name 'sum']params: [#Arguments [#Name 'Ps']]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Infix left: [#Name 's']name: [#Name '//']right: [#Tuple [#Infix left: [#Name 'n']name: [#Name '-']right: [#Int '2']]]]]]]]]
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '1'][#Name 'n']]]body: [#Block [#SelfAssignment left: [#Name 'n']name: [# '*=']right: [#Name 'i']]]][#VarDecl name: [#Name 'N']expr: [#ApplyExpr name: [#Name 'str']params: [#Arguments [#Name 'n']]]][#VarDecl name: [#Name 'l']expr: [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'N']]]][#VarDecl name: [#Name 's']expr: [#Int '0']][#For each: [# [#Name 'j']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Infix left: [#Name 'l']name: [#Name '-']right: [#Int '1']][#Unary name: [#Name '-']expr: [#Int '1']][#Unary name: [#Name '-']expr: [#Int '1']]]]body: [#Block [#If cond: [#Infix left: [#IndexExpr recv: [#Name 'N']index: [#Name 'j']]name: [#Name '==']right: [#QString '"0"']]then: [#Block [#SelfAssignment left: [#Name 's']name: [# '+=']right: [#Int '1']]]else: [#Else [#Block [#Break 'break']]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 's']]]]]]
Syntax Error ((unknown source):45:14+923)
    print(f"{x:.8f} {y:.8f}")
              ^              
# 入力された文字列の整数値をnとする
n = int(input())
# {{入力された文字列を空白で分割した列}}の各要素をaとし、aの整数値の列をAとする
A = [int(a) for a in input().split()]
# 'nから1を引いた値から-1未満までの-1間隔の数列の各要素を順にiとして、繰り返す
for i  in range(n - 1, -1, -1)  :
  # iが0のとき、
  if i == 0  :
    # A(i)を出力する
    print(A[i])
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#Name 'A']index: [#Name 'i']][#QString '" "'][#Data [#KeyValue name: [#Name 'sep']value: [#QString '""']][#KeyValue name: [#Name 'end']value: [#QString '""']]]]]]]]
# 0をsとする
s = 0
# '0から5未満までの数列の各要素を順にiとして、繰り返す
for i  in range(5)  :
  # 入力された文字列の整数値をpとする
  p = int(input())
  # pが40より小さいとき、
  if p < 40  :
    # ([[#Name 's'], [#Int '40']],)
    [[#Name 's'], [#Int '40']]
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 's']name: [# '+=']right: [#Name 'p']]]]
# sを5で割った商を出力する
print(s // 5)
# 空列をSiとする
Si = []
# 空列をSoとする
So = []
# '0から4未満までの数列の各要素を順にiとして、繰り返す
for i  in range(4)  :
  # 入力された文字列の整数値をpとする
  p = int(input())
  # Si.append(p)
  Si.append(p)
# '0から2未満までの数列の各要素を順にjとして、繰り返す
for j  in range(2)  :
  # 入力された文字列の整数値をpとする
  p = int(input())
  # So.append(p)
  So.append(p)
# {{Siの総和からSiの最小値を引いた値}}にSoの総和を加えた値からSoの最小値を引いた値をsとする
s = sum(Si) - min(Si) + sum(So) - min(So)
# sを出力する
print(s)
# 空列をWとする
W = []
# 空列をKとする
K = []
# '0から10未満までの数列の各要素を順にiとして、繰り返す
for i  in range(10)  :
  # W.append(int(input()))
  W.append(int(input()))
# '0から10未満までの数列の各要素を順にjとして、繰り返す
for j  in range(10)  :
  # K.append(int(input()))
  K.append(int(input()))
# Wと((reverse, 真))からなる辞書をソートした列をWsとする
Ws = sorted(W, reverse = True)
# Kと((reverse, 真))からなる辞書をソートした列をKsとする
Ks = sorted(K, reverse = True)
# 0をwとする
w = 0
# 0をkとする
k = 0
# '0から3未満までの数列の各要素を順にiとして、繰り返す
for i  in range(3)  :
  # ([[#Name 'w'], [#IndexExpr recv: [#Name 'Ws']index: [#Name 'i']]],)
  [[#Name 'w'], [#IndexExpr recv: [#Name 'Ws']index: [#Name 'i']]]
  # ([[#Name 'k'], [#IndexExpr recv: [#Name 'Ks']index: [#Name 'i']]],)
  [[#Name 'k'], [#IndexExpr recv: [#Name 'Ks']index: [#Name 'i']]]
# wとkを出力する
print(w, k)
# {{'1から31未満までの数列}}の各要素をiとし、iの列をAとする
A = [i for i in range(1, 31)]
# 空列をNとする
N = []
# '0から28未満までの数列の各要素を順にiとして、繰り返す
for i  in range(28)  :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # N.append(n)
  N.append(n)
# 'Aの集合からNの集合を引いた値のリストをRとする
R = list(set(A) - set(N))
# Rの最小値を出力する
print(min(R))
# Rの最大値を出力する
print(max(R))
# 入力された文字列の整数値をnとする
n = int(input())
# {{入力された文字列を空白で分割した列}}の各要素をxとし、xの整数値の列をXとする
X = [int(x) for x in input().split()]
# Xの最大値からXの最小値を引いた値をsubとする
sub = max(X) - min(X)
# subを2で割った余りが0のとき、
if sub % 2 == 0  :
  # subを2で割った商を出力する
  print(sub // 2)
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Infix left: [#Infix left: [#Name 'sub']name: [#Name '//']right: [#Int '2']]name: [#Name '+']right: [#Int '1']]]]]]]
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にnとkとする
  n, k  = map(int, input().split())
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'A']expr: [#List '[]']][#VarDecl name: [#Name 'S']expr: [#List '[]']][#VarDecl name: [#Name 's']expr: [#Int '0']][#VarDecl name: [#Name 'cnt']expr: [#Int '0']][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'n']]]body: [#Block [#Expression [#MethodExpr recv: [#Name 'A']name: [#Name 'append']params: [#Arguments [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]]]]]][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'k']]]body: [#Block [#SelfAssignment left: [#Name 's']name: [# '+=']right: [#IndexExpr recv: [#Name 'A']index: [#Name 'i']]]]][#Expression [#MethodExpr recv: [#Name 'S']name: [#Name 'append']params: [#Arguments [#Name 's']]]][#For each: [# [#Name 'j']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'k'][#Name 'n']]]body: [#Block [#VarDecl name: [#Name 's']expr: [#Infix left: [#Infix left: [#IndexExpr recv: [#Name 'S']index: [#Name 'cnt']]name: [#Name '-']right: [#IndexExpr recv: [#Name 'A']index: [#Infix left: [#Name 'j']name: [#Name '-']right: [#Name 'k']]]]name: [#Name '+']right: [#IndexExpr recv: [#Name 'A']index: [#Name 'j']]]][#Expression [#MethodExpr recv: [#Name 'S']name: [#Name 'append']params: [#Arguments [#Name 's']]]][#SelfAssignment left: [#Name 'cnt']name: [# '+=']right: [#Int '1']]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#ApplyExpr name: [#Name 'max']params: [#Arguments [#Name 'S']]]]]]]]
# 空列をMとする
M = []
# '0から10未満までの数列の各要素を順にiとして、繰り返す
for i  in range(10)  :
  # M.append(int(input()))
  M.append(int(input()))
# Mと((reverse, 真))からなる辞書をソートした列をMsとする
Ms = sorted(M, reverse = True)
# '0から3未満までの数列の各要素を順にjとして、繰り返す
for j  in range(3)  :
  # Ms(j)を出力する
  print(Ms[j])
Syntax Error ((unknown source):11:-1+147)
    except :
            
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'C']expr: [#List [#ForExpr append: [#Int '0']each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '10']]]]]][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'n']]]body: [#Block [#SelfAssignment left: [#IndexExpr recv: [#Name 'C']index: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]]name: [# '+=']right: [#Int '1']]]][#For each: [# [#Name 'j']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '10']]]body: [#Block [#If cond: [#Infix left: [#IndexExpr recv: [#Name 'C']index: [#Name 'j']]name: [#Name '==']right: [#Int '0']]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"-"']]]]]else: [#Else [#Block [#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#IndexExpr recv: [#Name 'C']index: [#Name 'j']]]]body: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"*"'][#Data [#KeyValue name: [#Name 'end']value: [#QString '""']]]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments '']]]]]]]]]]
# 入力された文字列を英大文字に変換した文字列を出力する
print(input().upper())
# 入力された文字列の英大文字を英小文字、英小文字を英大文字に変換した文字列を出力する
print(input().swapcase())
# "abcdefghijklmnopqrstuvwxyz"をaとする
a = "abcdefghijklmnopqrstuvwxyz"
# {{'0から26未満までの数列}}の各要素をiとし、0の列をAとする
A = [0 for i in range(26)]
# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 's']expr: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 's']]]]]body: [#Block [#If cond: [#Or left: [#Infix left: [#IndexExpr recv: [#Name 's']index: [#Name 'i']]name: [#Name 'in']right: [#Name 'a']]right: [#Infix left: [#MethodExpr recv: [#IndexExpr recv: [#Name 's']index: [#Name 'i']]name: [#Name 'lower']params: [#Arguments '']]name: [#Name 'in']right: [#Name 'a']]]then: [#Block [#SelfAssignment left: [#IndexExpr recv: [#Name 'A']index: [#MethodExpr recv: [#Name 'a']name: [#Name 'index']params: [#Arguments [#MethodExpr recv: [#IndexExpr recv: [#Name 's']index: [#Name 'i']]name: [#Name 'lower']params: [#Arguments '']]]]]name: [# '+=']right: [#Int '1']]]]]]]except: [# [#Except body: [#Block [#Break 'break']]]]]
# '0から26未満までの数列の各要素を順にjとして、繰り返す
for j  in range(26)  :
  # a(j)、":"、A(j)を出力する
  print(a[j], ":", A[j])
# 真の間、繰り返す
while True :
  # 入力された文字列をnとする
  n = input()
  # nが"0"のとき、
  if n == "0"  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 's']expr: [#Int '0']][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'n']]]]]body: [#Block [#SelfAssignment left: [#Name 's']name: [# '+=']right: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'n']index: [#Name 'i']]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 's']]]]]]
# 入力された文字列をnとする
n = input()
# ("K"、"U"、"P"、"C")からなる列をKUPCとする
KUPC = ["K", "U", "P", "C"]
# {{'0から4未満までの数列}}の各要素をiとし、0の列をkupcとする
kupc = [0 for i in range(4)]
# '0からnの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(n))  :
  # n(i)がKUPCに含まれるとき、
  if n[i] in KUPC  :
    # ([[#IndexExpr recv: [#Name 'kupc']index: [#MethodExpr recv: [#Name 'KUPC']name: [#Name 'index']params: [#Arguments [#IndexExpr recv: [#Name 'n']index: [#Name 'i']]]]], [#Int '1']],)
    [[#IndexExpr recv: [#Name 'kupc']index: [#MethodExpr recv: [#Name 'KUPC']name: [#Name 'index']params: [#Arguments [#IndexExpr recv: [#Name 'n']index: [#Name 'i']]]]], [#Int '1']]
# kupcの最小値を出力する
print(min(kupc))
# 入力された文字列をWとする
W = input()
# 0をcntとする
cnt = 0
# 真の間、繰り返す
while True :
  # 入力された文字列をtとする
  t = input()
  # tが"END_OF_TEXT"のとき、
  if t == "END_OF_TEXT"  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'T']expr: [#MethodExpr recv: [#Name 't']name: [#Name 'lower']params: [#Arguments '']]][#VarDecl name: [#Name 'T']expr: [#MethodExpr recv: [#Name 'T']name: [#Name 'split']params: [#Arguments '']]][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'T']]]]]body: [#Block [#If cond: [#Infix left: [#IndexExpr recv: [#Name 'T']index: [#Name 'i']]name: [#Name '==']right: [#Name 'W']]then: [#Block [#SelfAssignment left: [#Name 'cnt']name: [# '+=']right: [#Int '1']]]]]]]]
# cntを出力する
print(cnt)
# 入力された文字列をsとする
s = input()
# 入力された文字列をpとする
p = input()
# sに2を掛けた値をSとする
S = s * 2
# pがSに含まれるとき、
if p in S  :
  # "Yes"を出力する
  print("Yes")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"No"']]]]]]
# 入力された文字列をTとする
T = input()
# 入力された文字列をPとする
P = input()
# Pの長さをlとする
l = len(P)
# '0から{{Tの長さからlを引いた値}}に1を加えた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(T) - l + 1)  :
  # Tの位置iから位置{{iにlを加えた値}}までの部分がPのとき、
  if T[i : i + l] == P  :
    # iを出力する
    print(i)
# 真の間、繰り返す
while True :
  # 入力された文字列をCとする
  C = input()
  # Cが"-"のとき、
  if C == "-"  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'm']expr: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'm']]]body: [#Block [#VarDecl name: [#Name 'h']expr: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]][#VarDecl name: [#Name 'c']expr: [#SliceExpr recv: [#Name 'C']start: [#Int '0']end: [#Name 'h']]][#VarDecl name: [#Name 'C']expr: [#SliceExpr recv: [#Name 'C']start: [#Name 'h']end: [#Infix left: [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'C']]]name: [#Name '+']right: [#Int '1']]]][#SelfAssignment left: [#Name 'C']name: [# '+=']right: [#Name 'c']]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'C']]]]]]
# 入力された文字列の整数値をnとする
n = int(input())
# 0をtとする
t = 0
# 0をhとする
h = 0
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # map(str,入力された文字列を空白で分割した列)を展開し順にTとHとする
  T, H  = map(str, input().split())
  # TがHより大きいとき、
  if T > H  :
    # ([[#Name 't'], [#Int '3']],)
    [[#Name 't'], [#Int '3']]
  # ('TがHより小さい',)
  elif T < H  :
    # ([[#Name 'h'], [#Int '3']],)
    [[#Name 'h'], [#Int '3']]
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 't']name: [# '+=']right: [#Int '1']][#SelfAssignment left: [#Name 'h']name: [# '+=']right: [#Int '1']]]]
# tとhを出力する
print(t, h)
# 真の間、繰り返す
while True :
  # 入力された文字列をd1とする
  d1 = input()
  # d1が"0"のとき、
  if d1 == "0"  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'd2']expr: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]][#VarDecl name: [#Name 'd3']expr: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]][#VarDecl name: [#Name 'd1A']expr: [#MethodExpr recv: [#SliceExpr recv: [#Name 'd1']start: [#Int '1']end: [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'd1']]]]name: [#Name 'count']params: [#Arguments [#QString '"A"']]]][#VarDecl name: [#Name 'd1B']expr: [#Infix left: [#Infix left: [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'd1']]]name: [#Name '-']right: [#Name 'd1A']]name: [#Name '-']right: [#Int '1']]][#If cond: [#Infix left: [#IndexExpr recv: [#Name 'd2']index: [#Int '0']]name: [#Name '==']right: [#QString '"A"']]then: [#Block [#SelfAssignment left: [#Name 'd1A']name: [# '+=']right: [#Int '1']]]else: [#Else [#Block [#SelfAssignment left: [#Name 'd1B']name: [# '+=']right: [#Int '1']]]]][#VarDecl name: [#Name 'd2A']expr: [#MethodExpr recv: [#SliceExpr recv: [#Name 'd2']start: [#Int '1']end: [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'd2']]]]name: [#Name 'count']params: [#Arguments [#QString '"A"']]]][#VarDecl name: [#Name 'd2B']expr: [#Infix left: [#Infix left: [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'd2']]]name: [#Name '-']right: [#Name 'd2A']]name: [#Name '-']right: [#Int '1']]][#If cond: [#Infix left: [#IndexExpr recv: [#Name 'd3']index: [#Int '0']]name: [#Name '==']right: [#QString '"A"']]then: [#Block [#SelfAssignment left: [#Name 'd2A']name: [# '+=']right: [#Int '1']]]else: [#Else [#Block [#SelfAssignment left: [#Name 'd2B']name: [# '+=']right: [#Int '1']]]]][#VarDecl name: [#Name 'd3A']expr: [#MethodExpr recv: [#SliceExpr recv: [#Name 'd3']start: [#Int '1']end: [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'd3']]]]name: [#Name 'count']params: [#Arguments [#QString '"A"']]]][#VarDecl name: [#Name 'd3B']expr: [#Infix left: [#Infix left: [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'd3']]]name: [#Name '-']right: [#Name 'd3A']]name: [#Name '-']right: [#Int '1']]][#If cond: [#And left: [#Infix left: [#Name 'd3A']name: [#Name '>=']right: [#Int '10']]right: [#Infix left: [#Name 'd3B']name: [#Name '>=']right: [#Int '10']]]then: [#Block [#If cond: [#Infix left: [#Name 'd3A']name: [#Name '>']right: [#Name 'd3B']]then: [#Block [#SelfAssignment left: [#Name 'd3A']name: [# '+=']right: [#Int '1']]]else: [#Else [#Block [#SelfAssignment left: [#Name 'd3B']name: [# '+=']right: [#Int '1']]]]]]else: [#Else [#Block [#If cond: [#Infix left: [#Name 'd3A']name: [#Name '>']right: [#Name 'd3B']]then: [#Block [#SelfAssignment left: [#Name 'd3A']name: [# '+=']right: [#Int '1']]]else: [#Else [#Block [#SelfAssignment left: [#Name 'd3B']name: [# '+=']right: [#Int '1']]]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'd1A'][#Name 'd1B']]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'd2A'][#Name 'd2B']]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'd3A'][#Name 'd3B']]]]]]
Syntax Error ((unknown source):8:25+123)
print(f"{math.sqrt(x + y):.5f}")
                         ^      
Syntax Error ((unknown source):16:10+227)
print(f"{S:.5f} {L:.5f} {h:.5f}")
          ^                      
Syntax Error ((unknown source):19:14+315)
    print(f"{a:.5f}")
              ^      
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にm、f、rとする
  m, f, r  = map(int, input().split())
  # {{mが-1}}、かつ{{fが-1かどうか}}、かつrが-1のとき、
  if m == -1 and f == -1 and r == -1  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#If cond: [#Or left: [#Or left: [#Infix left: [#Name 'm']name: [#Name '==']right: [#Unary name: [#Name '-']expr: [#Int '1']]]right: [#Infix left: [#Name 'f']name: [#Name '==']right: [#Unary name: [#Name '-']expr: [#Int '1']]]]right: [#Infix left: [#Infix left: [#Name 'm']name: [#Name '+']right: [#Name 'f']]name: [#Name '<']right: [#Int '30']]]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"F"']]]]]elif: [# [#Elif cond: [#Infix left: [#Infix left: [#Name 'm']name: [#Name '+']right: [#Name 'f']]name: [#Name '>=']right: [#Int '80']]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"A"']]]]]][#Elif cond: [#And left: [#Infix left: [#Infix left: [#Name 'm']name: [#Name '+']right: [#Name 'f']]name: [#Name '>=']right: [#Int '65']]right: [#Infix left: [#Infix left: [#Name 'm']name: [#Name '+']right: [#Name 'f']]name: [#Name '<']right: [#Int '80']]]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"B"']]]]]][#Elif cond: [#And left: [#Infix left: [#Infix left: [#Name 'm']name: [#Name '+']right: [#Name 'f']]name: [#Name '>=']right: [#Int '50']]right: [#Infix left: [#Infix left: [#Name 'm']name: [#Name '+']right: [#Name 'f']]name: [#Name '<']right: [#Int '65']]]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"C"']]]]]]]else: [#Else [#Block [#If cond: [#Infix left: [#Name 'r']name: [#Name '>=']right: [#Int '50']]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"C"']]]]]else: [#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"D"']]]]]]]]]]]]
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にnとxとする
  n, x  = map(int, input().split())
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'cnt']expr: [#Int '0']][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '1'][#Infix left: [#Name 'n']name: [#Name '-']right: [#Int '1']]]]body: [#Block [#For each: [# [#Name 'j']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Infix left: [#Name 'i']name: [#Name '+']right: [#Int '1']][#Name 'n']]]body: [#Block [#For each: [# [#Name 'k']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Infix left: [#Name 'j']name: [#Name '+']right: [#Int '1']][#Infix left: [#Name 'n']name: [#Name '+']right: [#Int '1']]]]body: [#Block [#If cond: [#Infix left: [#Infix left: [#Infix left: [#Name 'i']name: [#Name '+']right: [#Name 'j']]name: [#Name '+']right: [#Name 'k']]name: [#Name '==']right: [#Name 'x']]then: [#Block [#SelfAssignment left: [#Name 'cnt']name: [# '+=']right: [#Int '1']]]]]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'cnt']]]]]]
# 入力された文字列の整数値をnとする
n = int(input())
# {{'1から14未満までの数列}}の各要素をiとし、iの列をSとする
S = [i for i in range(1, 14)]
# {{'1から14未満までの数列}}の各要素をiとし、iの列をHとする
H = [i for i in range(1, 14)]
# {{'1から14未満までの数列}}の各要素をiとし、iの列をCとする
C = [i for i in range(1, 14)]
# {{'1から14未満までの数列}}の各要素をiとし、iの列をDとする
D = [i for i in range(1, 14)]
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # map(str,入力された文字列を空白で分割した列)を展開し順にmとrとする
  m, r  = map(str, input().split())
  # mが"S"のとき、
  if m == "S"  :
    # Sからrの整数値を取り除いた集まり
    S.remove(int(r))
  # ('mが"H"の',)
  elif m == "H"  :
    # Hからrの整数値を取り除いた集まり
    H.remove(int(r))
  # ('mが"C"の',)
  elif m == "C"  :
    # Cからrの整数値を取り除いた集まり
    C.remove(int(r))
  # ()
  else :[#Else [#Block [#Expression [#MethodExpr recv: [#Name 'D']name: [#Name 'remove']params: [#Arguments [#ApplyExpr name: [#Name 'int']params: [#Arguments [#Name 'r']]]]]]]]
# Sの長さが0より大きいとき、
if len(S) > 0  :
  # '0からSの長さ未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(len(S))  :
    # "S"とS(i)を出力する
    print("S", S[i])
# Hの長さが0より大きいとき、
if len(H) > 0  :
  # '0からHの長さ未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(len(H))  :
    # "H"とH(i)を出力する
    print("H", H[i])
# Cの長さが0より大きいとき、
if len(C) > 0  :
  # '0からCの長さ未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(len(C))  :
    # "C"とC(i)を出力する
    print("C", C[i])
# Dの長さが0より大きいとき、
if len(D) > 0  :
  # '0からDの長さ未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(len(D))  :
    # "D"とD(i)を出力する
    print("D", D[i])
# map(整数,入力された文字列を空白で分割した列)を展開し順にnとmとする
n, m  = map(int, input().split())
# 空列をAとする
A = []
# 空列をBとする
B = []
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # A.append([int(a) for a in input().split()])
  A.append([int(a) for a in input().split()])
# '0からm未満までの数列の各要素を順にjとして、繰り返す
for j  in range(m)  :
  # B.append(int(input()))
  B.append(int(input()))
# 空列をCとする
C = []
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # 0をcとする
  c = 0
  # '0からm未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(m)  :
    # ([[#Name 'c'], [#Infix left: [#IndexExpr recv: [#IndexExpr recv: [#Name 'A']index: [#Name 'i']]index: [#Name 'j']]name: [#Name '*']right: [#IndexExpr recv: [#Name 'B']index: [#Name 'j']]]],)
    [[#Name 'c'], [#Infix left: [#IndexExpr recv: [#IndexExpr recv: [#Name 'A']index: [#Name 'i']]index: [#Name 'j']]name: [#Name '*']right: [#IndexExpr recv: [#Name 'B']index: [#Name 'j']]]]
  # C.append(c)
  C.append(c)
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # C(i)を出力する
  print(C[i])
# map(整数,入力された文字列を空白で分割した列)を展開し順にn、m、lとする
n, m, l  = map(int, input().split())
# 空列をAとする
A = []
# 空列をBとする
B = []
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # A.append([int(a) for a in input().split()])
  A.append([int(a) for a in input().split()])
# '0からm未満までの数列の各要素を順にjとして、繰り返す
for j  in range(m)  :
  # B.append([int(b) for b in input().split()])
  B.append([int(b) for b in input().split()])
# 空列をCとする
C = []
# 空列をLとする
L = []
# 0をsとする
s = 0
# '0からl未満までの数列の各要素を順にiとして、繰り返す
for i  in range(l)  :
  # '0からn未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(n)  :
    # '0からm未満までの数列の各要素を順にkとして、繰り返す
    for k  in range(m)  :
      # ([[#Name 's'], [#Infix left: [#IndexExpr recv: [#IndexExpr recv: [#Name 'A']index: [#Name 'j']]index: [#Name 'k']]name: [#Name '*']right: [#IndexExpr recv: [#IndexExpr recv: [#Name 'B']index: [#Name 'k']]index: [#Name 'i']]]],)
      [[#Name 's'], [#Infix left: [#IndexExpr recv: [#IndexExpr recv: [#Name 'A']index: [#Name 'j']]index: [#Name 'k']]name: [#Name '*']right: [#IndexExpr recv: [#IndexExpr recv: [#Name 'B']index: [#Name 'k']]index: [#Name 'i']]]]
    # L.append(s)
    L.append(s)
    # 0をsとする
    s = 0
  # C.append(L[i * n : i * n + n])
  C.append(L[i * n : i * n + n])
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # '0からl未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(l)  :
    # jがlから1を引いた値のとき、
    if j == l - 1  :
      # C(j)(i)を出力する
      print(C[j][i])
    # ()
    else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#IndexExpr recv: [#Name 'C']index: [#Name 'j']]index: [#Name 'i']][#Data [#KeyValue name: [#Name 'end']value: [#QString '" "']]]]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にrとcとする
r, c  = map(int, input().split())
# 空列をAとする
A = []
# '0からr未満までの数列の各要素を順にiとして、繰り返す
for i  in range(r)  :
  # A.append([int(a) for a in input().split()])
  A.append([int(a) for a in input().split()])
  # A[i].append(sum(A[i]))
  A[i].append(sum(A[i]))
# 空列をSとする
S = []
# '0からcに1を加えた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(c + 1)  :
  # 0をsとする
  s = 0
  # '0からr未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(r)  :
    # ([[#Name 's'], [#IndexExpr recv: [#IndexExpr recv: [#Name 'A']index: [#Name 'j']]index: [#Name 'i']]],)
    [[#Name 's'], [#IndexExpr recv: [#IndexExpr recv: [#Name 'A']index: [#Name 'j']]index: [#Name 'i']]]
  # S.append(s)
  S.append(s)
# A.append(S)
A.append(S)
# '0からrに1を加えた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(r + 1)  :
  # '0からcに1を加えた値未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(c + 1)  :
    # jがcのとき、
    if j == c  :
      # A(i)(j)を出力する
      print(A[i][j])
    # ()
    else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#IndexExpr recv: [#Name 'A']index: [#Name 'i']]index: [#Name 'j']][#Data [#KeyValue name: [#Name 'end']value: [#QString '" "']]]]]]]]
Syntax Error ((unknown source):14:11+195)
print(f"{d1:.6f}")
           ^      
# 入力された文字列の整数値をnとする
n = int(input())
# nをnnとする
nn = n
# 空列をNとする
N = []
# n、":"、((sep, "")と(end, " "))からなる辞書を出力する
print(n, ":", sep = "", end = " ") 
# nを2で割った余りが0のとき、
if n % 2 == 0  :
  # nを2で割った余りが0の間、繰り返す
  while n % 2 == 0  :
    # N.append(2)
    N.append(2)
    # ([[#Name 'n'], [#Int '2']],)
    [[#Name 'n'], [#Int '2']]
# '3からnnの(1 / 2)の組乗の整数値に1を加えた値未満までの2間隔の数列の各要素を順にiとして、繰り返す
for i  in range(3, int(nn ** (1 / 2)) + 1, 2)  :
  # nをiで割った余りが0の間、繰り返す
  while n % i == 0  :
    # N.append(i)
    N.append(i)
    # ([[#Name 'n'], [#Name 'i']],)
    [[#Name 'n'], [#Name 'i']]
# nが1と等しくないとき、
if n != 1  :
  # N.append(n)
  N.append(n)
# Nの長さが0のとき、
if len(N) == 0  :
  # nを出力する
  print(n)
# ()
else :[#Else [#Block [#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'N']]]]]body: [#Block [#If cond: [#Infix left: [#Name 'i']name: [#Name '==']right: [#Infix left: [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'N']]]name: [#Name '-']right: [#Int '1']]]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#Name 'N']index: [#Name 'i']]]]]]else: [#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#Name 'N']index: [#Name 'i']][#Data [#KeyValue name: [#Name 'sep']value: [#QString '""']][#KeyValue name: [#Name 'end']value: [#QString '" "']]]]]]]]]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にmとnとする
m, n  = map(int, input().split())
# 1000000007をmodとする
mod = 1000000007
# mのn乗に対するmodの剰余を出力する
print(pow(m, n, mod))
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
  a, b  = map(int, input().split())
  # aが0のとき、
  if a == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#If cond: [#Infix left: [#Name 'a']name: [#Name '<=']right: [#Name 'b']]then: [#Block [#MultiAssignment left: [# [#Name 'X'][#Name 'Y']]right: [#Tuple [#Name 'b'][#Name 'a']]]]else: [#Else [#Block [#MultiAssignment left: [# [#Name 'X'][#Name 'Y']]right: [#Tuple [#Name 'a'][#Name 'b']]]]]][#VarDecl name: [#Name 'cnt']expr: [#Int '0']][#FuncDecl name: [#Name 'Euc']params: [#FuncParam [#ParamDecl name: [#Name 'X']][#ParamDecl name: [#Name 'Y']][#ParamDecl name: [#Name 'cnt']]]body: [#Block [#While cond: [#Infix left: [#Name 'Y']name: [#Name '!=']right: [#Int '0']]body: [#Block [#SelfAssignment left: [#Name 'cnt']name: [# '+=']right: [#Int '1']][#SelfAssignment left: [#Name 'X']name: [# '%=']right: [#Name 'Y']][#MultiAssignment left: [# [#Name 'X'][#Name 'Y']]right: [#Tuple [#Name 'Y'][#Name 'X']]]]][#Return expr: [#Tuple [#Name 'X'][#Name 'cnt']]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#ApplyExpr name: [#Name 'Euc']params: [#Arguments [#Name 'X'][#Name 'Y'][#Name 'cnt']]]index: [#Int '0']][#IndexExpr recv: [#ApplyExpr name: [#Name 'Euc']params: [#Arguments [#Name 'X'][#Name 'Y'][#Name 'cnt']]]index: [#Int '1']]]]]]]
# mathモジュールを用いる
import math
# 入力された文字列の整数値をnとする
n = int(input())
# {{入力された文字列を空白で分割した列}}の各要素をaとし、aの整数値の列をAとする
A = [int(a) for a in input().split()]
# Aの最初値をansとする
ans = A[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1, n)  :
  # ansにA(i)を掛けた値をmath.gcd(ans, A[i])で割った商をansとする
  ans = ans * A[i] // math.gcd(ans, A[i])
# ansを出力する
print(ans)
# mathモジュールを用いる
import math
# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x, y  = map(int, input().split())
# math.gcd(x, y)を出力する
print(math.gcd(x, y))
# mathモジュールを用いる
import math
# 入力された文字列の整数値をnとする
n = int(input())
# 0をcntとする
cnt = 0
# 関数primeを[#FuncParam [#ParamDecl name: [#Name 'a']]]のパラメータを持つように定義する
def prime (a)  :
  # '2からmath.sqrt(a)の整数値に1を加えた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(2, int(math.sqrt(a)) + 1)  :
    # aをiで割った余りが0のとき、
    if a % i == 0  :
      # 偽を関数出力とする
      return False
  # 真を関数出力とする
  return True
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # prime(入力された文字列の整数値)のとき、
  if prime(int(input()))  :
    # ([[#Name 'cnt'], [#Int '1']],)
    [[#Name 'cnt'], [#Int '1']]
# cntを出力する
print(cnt)
Syntax Error ((unknown source):43:-1+757)
    except :
            
Syntax Error ((unknown source):27:0+403)
# Listからnumに最も近い値を返す
^                              
Syntax Error ((unknown source):14:18+229)
            elif n % 2 == 0 :
                  ^          
Syntax Error ((unknown source):14:-1+241)
    except :
            
Syntax Error ((unknown source):13:18+297)
        print(f"{x:.3f} {y:.3f}")
                  ^              
Syntax Error ((unknown source):8:-1+77)
    else :
          
Syntax Error ((unknown source):21:-1+354)
    except :
            
# reモジュールを用いる
import re
# 入力された文字列を空白で分割した列をIとする
I = input().split()
# 空列をSとする
S = []
# '0からIの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(I))  :
  # 文字列I(i)を正規表現"[,.]"で分割した文字列リストをI[i] にする
  I[i]  = re.split("[,.]", I[i])
  # 2がI(i)の最初値の長さより小さく、かつI(i)の最初値の長さが7より小さいとき、
  if 2 < len(I[i][0]) and len(I[i][0]) < 7  :
    # S.append(I[i][0])
    S.append(I[i][0])
# '0からSの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(S))  :
  # iがSの長さから1を引いた値のとき、
  if i == len(S) - 1  :
    # S(i)を出力する
    print(S[i])
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#Name 'S']index: [#Name 'i']][#QString '" "'][#Data [#KeyValue name: [#Name 'sep']value: [#QString '""']][#KeyValue name: [#Name 'end']value: [#QString '""']]]]]]]]
# 入力された文字列をSとする
S = input()
# -1をcntとする
cnt = -1
# '0からSの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(S))  :
  # iがSの長さから1を引いた値のとき、
  if i == len(S) - 1  :
    # Sの最初値を出力する
    print(S[0])
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#Name 'S']index: [#Name 'cnt']][#Data [#KeyValue name: [#Name 'sep']value: [#QString '""']][#KeyValue name: [#Name 'end']value: [#QString '""']]]]]][#SelfAssignment left: [#Name 'cnt']name: [# '-=']right: [#Int '1']]]]
Syntax Error ((unknown source):8:-1+92)
    else :
          
Syntax Error ((unknown source):8:-1+111)
    else :
          
Syntax Error ((unknown source):17:-1+307)
    except :
            
Syntax Error ((unknown source):12:-1+163)
    except :
            
# {{'65から{{65に26を加えた値}}未満までの数列}}の各要素をiとし、文字コードiの文字の列をAとする
A = [chr(i) for i in range(65, 65 + 26)][#Document [# 'アルファベット大文字一覧表']]
# {{'68から{{68に23を加えた値}}未満までの数列}}の各要素をiとし、文字コードiの文字の列をDとする
D = [chr(i) for i in range(68, 68 + 23)]
# D.append("A")
D.append("A")
# D.append("B")
D.append("B")
# D.append("C")
D.append("C")[#Document [# 'シーザー暗号変換後アルファベット大文字一覧表']]
# 入力された文字列をnとする
n = input()
# 空列をANSとする
ANS = []
# '0からnの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(n))  :
  # ANS.append(A[D.index(n[i])])
  ANS.append(A[D.index(n[i])])
# '0からANSの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(ANS))  :
  # iがANSの長さから1を引いた値のとき、
  if i == len(ANS) - 1  :
    # ANS(i)を出力する
    print(ANS[i])
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#Name 'ANS']index: [#Name 'i']][#Data [#KeyValue name: [#Name 'end']value: [#QString '""']]]]]]]]
# 入力された文字列を空白で分割した列をSとする
S = input().split()
# 0をlとする
l = 0
# 0をnとする
n = 0
# "a"をLとする
L = "a"
# "a"をNとする
N = "a"
# '0からSの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(S))  :
  # S内のS(i)の出現をカウントした整数がnより大きいとき、
  if S.count(S[i]) > n  :
    # S内のS(i)の出現をカウントした整数をnとする
    n = S.count(S[i])
    # S(i)をNとする
    N = S[i]
# '0からSの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(S))  :
  # S(i)の長さがlより大きいとき、
  if len(S[i]) > l  :
    # S(i)の長さをlとする
    l = len(S[i])
    # S(i)をLとする
    L = S[i]
# NとLを出力する
print(N, L)
# 入力された文字列をsとする
s = input()
# 空列をSとする
S = []
# "apple"をaとする
a = "apple"
# "peach"をpとする
p = "peach"
# 空列をAとする
A = []
# 空列をPとする
P = []
# '0からsの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(s))  :
  # S.append(s[i])
  S.append(s[i])
# '0から5未満までの数列の各要素を順にiとして、繰り返す
for i  in range(5)  :
  # A.append(a[i])
  A.append(a[i])
  # P.append(p[i])
  P.append(p[i])
# '0からSの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(S))  :
  # Sの位置iから位置{{iに5を加えた値}}までの部分がAのとき、
  if S[i : i + 5] == A  :
    # PをS[i : i + 5] にする
    S[i : i + 5]  = P
  # ('Sの位置iから位置{{iに5を加えた値}}までの部分がPの',)
  elif S[i : i + 5] == P  :
    # AをS[i : i + 5] にする
    S[i : i + 5]  = A
# '0からSの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(S))  :
  # iがSの長さから1を引いた値のとき、
  if i == len(S) - 1  :
    # S(i)を出力する
    print(S[i])
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#Name 'S']index: [#Name 'i']][#Data [#KeyValue name: [#Name 'sep']value: [#QString '""']][#KeyValue name: [#Name 'end']value: [#QString '""']]]]]]]]
Syntax Error ((unknown source):15:-1+202)
    except :
            
Syntax Error ((unknown source):13:18+260)
            elif B[i] in A :
                  ^         
Syntax Error ((unknown source):8:-1+100)
    else :
          
Syntax Error ((unknown source):10:-1+117)
    else :
          
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にx、y、sとする
  x, y, s  = map(int, input().split())
  # xが0のとき、
  if x == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'ans']expr: [#Int '0']][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '1'][#Infix left: [#Infix left: [#Name 's']name: [#Name '//']right: [#Int '2']]name: [#Name '+']right: [#Int '1']]]]body: [#Block [#For each: [# [#Name 'j']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Infix left: [#Name 's']name: [#Name '-']right: [#Int '1']][#Int '1'][#Unary name: [#Name '-']expr: [#Int '1']]]]body: [#Block [#If cond: [#Infix left: [#Infix left: [#Tuple [#Infix left: [#Infix left: [#Name 'i']name: [#Name '*']right: [#Tuple [#Infix left: [#Int '100']name: [#Name '+']right: [#Name 'x']]]]name: [#Name '//']right: [#Int '100']]]name: [#Name '+']right: [#Tuple [#Infix left: [#Infix left: [#Name 'j']name: [#Name '*']right: [#Tuple [#Infix left: [#Int '100']name: [#Name '+']right: [#Name 'x']]]]name: [#Name '//']right: [#Int '100']]]]name: [#Name '==']right: [#Name 's']]then: [#Block [#VarDecl name: [#Name 'Y']expr: [#Infix left: [#Tuple [#Infix left: [#Infix left: [#Name 'i']name: [#Name '*']right: [#Tuple [#Infix left: [#Int '100']name: [#Name '+']right: [#Name 'y']]]]name: [#Name '//']right: [#Int '100']]]name: [#Name '+']right: [#Tuple [#Infix left: [#Infix left: [#Name 'j']name: [#Name '*']right: [#Tuple [#Infix left: [#Int '100']name: [#Name '+']right: [#Name 'y']]]]name: [#Name '//']right: [#Int '100']]]]][#If cond: [#Infix left: [#Name 'ans']name: [#Name '<']right: [#Name 'Y']]then: [#Block [#VarDecl name: [#Name 'ans']expr: [#Name 'Y']]]]]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'ans']]]]]]
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にnとmとする
  n, m  = map(int, input().split())
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'g']expr: [#ApplyExpr name: [#Name 'list']params: [#Arguments [#ApplyExpr name: [#Name 'map']params: [#Arguments [#Name 'int'][#MethodExpr recv: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]]]]]][#VarDecl name: [#Name 'g_sort']expr: [#ApplyExpr name: [#Name 'sorted']params: [#Arguments [#Name 'g']]]][#If cond: [#Infix left: [#Infix left: [#IndexExpr recv: [#Name 'g_sort']index: [#Int '0']]name: [#Name '+']right: [#IndexExpr recv: [#Name 'g_sort']index: [#Int '1']]]name: [#Name '>']right: [#Name 'm']]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString "'NONE'"]]]]]else: [#Else [#Block [#VarDecl name: [#Name 'ans']expr: [#Int '0']][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Infix left: [#Name 'n']name: [#Name '-']right: [#Int '1']][#Int '0'][#Unary name: [#Name '-']expr: [#Int '1']]]]body: [#Block [#For each: [# [#Name 'j']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Infix left: [#Name 'i']name: [#Name '-']right: [#Int '1']][#Unary name: [#Name '-']expr: [#Int '1']][#Unary name: [#Name '-']expr: [#Int '1']]]]body: [#Block [#VarDecl name: [#Name 's']expr: [#Infix left: [#IndexExpr recv: [#Name 'g_sort']index: [#Name 'i']]name: [#Name '+']right: [#IndexExpr recv: [#Name 'g_sort']index: [#Name 'j']]]][#If cond: [#And left: [#Infix left: [#Name 's']name: [#Name '>']right: [#Name 'ans']]right: [#Infix left: [#Name 's']name: [#Name '<=']right: [#Name 'm']]]then: [#Block [#VarDecl name: [#Name 'ans']expr: [#Name 's']]]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'ans']]]]]]]]]
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'a']expr: [#ApplyExpr name: [#Name 'list']params: [#Arguments [#ApplyExpr name: [#Name 'map']params: [#Arguments [#Name 'int'][#MethodExpr recv: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]]]]]][#VarDecl name: [#Name 'ave']expr: [#Infix left: [#ApplyExpr name: [#Name 'sum']params: [#Arguments [#Name 'a']]]name: [#Name '/']right: [#Name 'n']]][#VarDecl name: [#Name 'b']expr: [#List [#ForExpr append: [#Name 'i']each: [# [#Name 'i']]list: [#Name 'a']cond: [#Infix left: [#Name 'i']name: [#Name '<=']right: [#Name 'ave']]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'b']]]]]]]]
# mathモジュールを用いる
import math
# 空列をPとする
P = [][#Document [# '素数一覧リスト']]
# 123456に2を掛けた値をMaxとする
Max = 123456 * 2
# 関数Eraを[#FuncParam [#ParamDecl name: [#Name 'P']][#ParamDecl name: [#Name 'Max']]]のパラメータを持つように定義する
def Era (P, Max)  :
  # ''2からMax未満までの数列のリストをDとする
  D = list(range(2, Max))
  # math.sqrt(Max)をlimitとする
  limit = math.sqrt(Max)
  # 真の間、繰り返す
  while True :
    # Dの最初値をpとする
    p = D[0]
    # limitがp以下のとき、
    if limit <= p  :
      # ([[#Name 'P'], [#Name 'D']],)
      [[#Name 'P'], [#Name 'D']]
      # Pを関数出力とする
      return P
    # P.append(p)
    P.append(p)
    # Dの各要素をdとし、{{{{dをpで割った余り}}が0と等しくない}}ときのdの列をDとする
    D = [d for d in D if d % p != 0][#Document [# 'D に含まれる値かつ p で割り切れない値をリスト化']]
# Era(P,Max)をeとする
e = Era(P, Max)
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'p']expr: [#List [#ForExpr append: [#Name 'i']each: [# [#Name 'i']]list: [#Name 'e']cond: [#Infix left: [#Infix left: [#Name 'n']name: [#Name '<']right: [#Name 'i']]name: [#Name '<=']right: [#Infix left: [#Int '2']name: [#Name '*']right: [#Name 'n']]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'p']]]]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にN、T、Eとする
N, T, E  = map(int, input().split())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをXとする
X = list(map(int, input().split()))
# '{{TからEを引いた値}}から{{{{TにEを加えた値}}に1を加えた値}}未満までの数列の各要素をiとし、iの列をtimeとする
time = [i for i in range(T - E, T + E + 1)]
# -2をclockとする
clock = -2
# '0からXの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(X))  :
  # '0からtimeの長さ未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(len(time))  :
    # time(j)をX(i)で割った余りが0のとき、
    if time[j] % X[i] == 0  :
      # X.index(X[i])をclockとする
      clock = X.index(X[i])
# clockに1を加えた値を出力する
print(clock + 1)
Syntax Error ((unknown source):19:-1+285)
    else :
          
Syntax Error ((unknown source):10:-1+149)
    else :
          
Syntax Error ((unknown source):8:-1+85)
    else :
          
# 真の間、繰り返す
while True :
  # 0をhantei3をhantei2とするとするをhantei1とする
  hantei1 = hantei2=  hantei3 = 0
  # 入力された文字列をnとする
  n = input()
  # nが'.'のとき、
  if n == '.' :
    # 繰り返すのを中断する
    break
  # 'nのリストをl_nとする
  l_n = list(n)
  # l_nの長さをlennとする
  lenn = len(l_n)
  # 空列をkakkoとする
  kakko = []
  # kakkoの長さをlenkakkoとする
  lenkakko = len(kakko)
  # '0からlenn未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(lenn) :
    # {{l_n内の'('の出現をカウントした整数}}が{{l_n内の')'の出現をカウントした整数}}と等しくなく、または{{l_n内の'['の出現をカウントした整数}}が{{l_n内の']'の出現をカウントした整数}}と等しくないとき、
    if l_n.count('(') != l_n.count(')') or l_n.count('[') != l_n.count(']') :
      # 'no'を出力する
      print('no')
      # ([[#Name 'hantei1'], [#Int '1']],)
      [[#Name 'hantei1'], [#Int '1']]
      # 繰り返すのを中断する
      break
    # l_n(i)が'('のとき、
    if l_n[i] == '(' :
      # kakko.append('maru')
      kakko.append('maru')
    # l_n(i)が'['のとき、
    if l_n[i] == '[' :
      # kakko.append('shikaku')
      kakko.append('shikaku')
    # kakkoの長さが0と等しくないとき、
    if len(kakko) != 0 :
      # kakko(-1)が'maru'のとき、
      if kakko[-1] == 'maru' :
        # l_n(i)が']'のとき、
        if l_n[i] == ']' :
          # 'no'を出力する
          print('no')
          # ([[#Name 'hantei1'], [#Int '1']],)
          [[#Name 'hantei1'], [#Int '1']]
          # 繰り返すのを中断する
          break
      # kakko(-1)が'shikaku'のとき、
      if kakko[-1] == 'shikaku' :
        # l_n(i)が')'のとき、
        if l_n[i] == ')' :
          # 'no'を出力する
          print('no')
          # ([[#Name 'hantei1'], [#Int '1']],)
          [[#Name 'hantei1'], [#Int '1']]
          # 繰り返すのを中断する
          break
      # l_n(i)が')'、またはl_n(i)が']'のとき、
      if l_n[i] == ')' or l_n[i] == ']' :
        # kakko.pop(-1)
        kakko.pop(-1)
    # ()
    else :[#Else [#Block [#If cond: [#Or left: [#Infix left: [#IndexExpr recv: [#Name 'l_n']index: [#Name 'i']]name: [#Name '==']right: [#QString "')'"]]right: [#Infix left: [#IndexExpr recv: [#Name 'l_n']index: [#Name 'i']]name: [#Name '==']right: [#QString "']'"]]]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString "'no'"]]]][#SelfAssignment left: [#Name 'hantei1']name: [# '+=']right: [#Int '1']][#Break 'break']]]]]
  # hantei1が0のとき、
  if hantei1 == 0 :
    # 'yes'を出力する
    print('yes')
Syntax Error ((unknown source):10:-1+95)
    else :
          
Syntax Error ((unknown source):6:-1+69)
    except :
            
Syntax Error ((unknown source):17:-1+282)
        elif(n > 2000) :
                        
Syntax Error ((unknown source):3:10+28)
@functools.lru_cache(maxsize = 30)
          ^                       