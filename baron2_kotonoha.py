
# "Hello World"を出力する
print("Hello World")
# 入力された文字列の整数値をaとする
a = int(input())
# aの3乗をxとする
x = a**3
# xを出力する
print(x)
# 入力された文字列の整数値をWとする
W = int(input())
# Wに32を掛けた値をxとする
x = W*32
# xを出力する
print(x)
# 入力された文字列の整数値をFとする
F = int(input())
# ({{Fから30を引いた値}})の組を2で割った商をCとする
C = (F-30)//2
# Cを出力する
print(C)
# map(整数,入力された文字列を空白で分割した列)を展開し順にp、m、cとする
p,m,c = map(int,input().split())
# pにmを加えた値にcを加えた値をxとする
x = p+m+c
# xを出力する
print(x)
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a,b = map(int,input().split())
# aにbを掛けた値をxとする
x = a*b
# 2に({{aにbを加えた値}})の組を掛けた値をyとする
y = 2*(a+b)
# [#Format [#Name 'x'][#StringPart ' '][#Name 'y']]を出力する
print(f"{x} {y}")
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a,b = map(int,input().split())
# aがbより大きいとき、
if a>b :
  # "a > b"を出力する
  print("a > b")
# ('aがbの',)
elif a==b :
  # "a == b"を出力する
  print("a == b")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"a < b"']]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a,b,c = map(int,input().split())
# aがbより小さいかどうかがcより小さいとき、
if a < b < c :
  # "Yes"を出力する
  print("Yes")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"No"']]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a,b  = map(int,input().split())
# ({{aにbを加えた値}})の組を2で割った商をxとする
x = (a+b)//2
# xを出力する
print(x)
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a,b  = map(int,input().split())
# aからbを引いた値の絶対値をxとする
x = abs(a-b)
# xを出力する
print(x)
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a,b,c  = map(int,input().split())
# aがc、またはbがcのとき、
if a == c or b == c :
  # "Close"を出力する
  print("Close")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"Open"']]]]]]
# 入力された文字列の整数値をSとする
S = int(input())
# Sを(60の2乗)の組で割った商をhとする
h = S//(60**2)
# ({{Sから{{hに60の2乗を掛けた値}}を引いた値}})の組を60で割った商をmとする
m = (S-h*60**2)//60
# Sから({{{{hに60の2乗を掛けた値}}に{{mに60を掛けた値}}を加えた値}})の組を引いた値をsとする
s = S-(h*60**2+m*60)
# [#Format [#Name 'h'][#StringPart ':'][#Name 'm'][#StringPart ':'][#Name 's']]を出力する
print(f"{h}:{m}:{s}")
Syntax Error ((unknown source):5:18+87)
print(f"{x} {y} {z:.08f}")
                  ^       
# mathモジュールを用いる
import math
# 入力された文字列の浮動小数点数値をrとする
r = float(input())
# format({{{{rにrを掛けた値}}にmath.piを掛けた値}})とformat({{{{2にrを掛けた値}}にmath.piを掛けた値}})を出力する
print("{0:.6f}".format(r*r*math.pi),"{0:.6f}".format(2*r*math.pi))	
Syntax Error ((unknown source):3:10+58)
print(f"{x:0.6f}")
          ^       
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# a.sort()
a.sort()
# map(str,a)を文字列' 'で連結した文字列を出力する
print(' '.join(map(str, a)))
# map(整数,入力された文字列を空白で分割した列)を展開し順にW、H、x、y、rとする
W,H,x,y,r  = map(int,input().split())
# {{xにrを加えた値}}がWより大きく、または{{yにrを加えた値}}がHより大きいとき、
if x+r > W or y+r > H :
  # "No"を出力する
  print("No")
# ('{{xからrを引いた値}}が0より小さく、または{{yからrを引いた値}}が0より小さい',)
elif x-r < 0 or y-r < 0 :
  # "No"を出力する
  print("No")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"Yes"']]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、c、dとする
a,b,c,d  = map(int,input().split())
# {{aがb}}、かつ{{cがdかどうか}}、または{{aがc}}、かつ{{bがdかどうか}}、または{{aがd}}、かつ{{bがcかどうか}}のとき、
if a == b and c == d or a == c and b == d or a == d and b == c :
  # "yes"を出力する
  print("yes")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"no"']]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にN、A、B、C、Dとする
N,A,B,C,D  = map(int,input().split())
# NをAで割った余りが0のとき、
if N % A == 0  :
  # NをAで割った商をaとする
  a = N // A
# ()
else :[#Else [#Block [#VarDecl name: [#Name 'a']expr: [#Infix left: [#Tuple [#Infix left: [#Name 'N']name: [#Name '//']right: [#Name 'A']]]name: [#Name '+']right: [#Int '1']]]]]
# NをCで割った余りが0のとき、
if N % C == 0 :
  # NをCで割った商をcとする
  c = N // C
# ()
else :[#Else [#Block [#VarDecl name: [#Name 'c']expr: [#Infix left: [#Tuple [#Infix left: [#Name 'N']name: [#Name '//']right: [#Name 'C']]]name: [#Name '+']right: [#Int '1']]]]]
# aにBを掛けた値をxとする
x = a*B
# cにDを掛けた値をyとする
y = c*D
# xがy以下のとき、
if x <= y :
  # xを出力する
  print(x)
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'y']]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a,b,c  = map(int,input().split())
# 0をxとする
x = 0
# ([[#Name 'x'], [#Infix left: [#Infix left: [#Name 'c']name: [#Name '//']right: [#Tuple [#Infix left: [#Infix left: [#Name 'a']name: [#Name '*']right: [#Int '7']]name: [#Name '+']right: [#Name 'b']]]]name: [#Name '*']right: [#Int '7']]],)
[[#Name 'x'], [#Infix left: [#Infix left: [#Name 'c']name: [#Name '//']right: [#Tuple [#Infix left: [#Infix left: [#Name 'a']name: [#Name '*']right: [#Int '7']]name: [#Name '+']right: [#Name 'b']]]]name: [#Name '*']right: [#Int '7']]]
# ([[#Name 'c'], [#Tuple [#Infix left: [#Infix left: [#Name 'a']name: [#Name '*']right: [#Int '7']]name: [#Name '+']right: [#Name 'b']]]],)
[[#Name 'c'], [#Tuple [#Infix left: [#Infix left: [#Name 'a']name: [#Name '*']right: [#Int '7']]name: [#Name '+']right: [#Name 'b']]]]
# ([[#Name 'x'], [#ApplyExpr name: [#Name 'min']params: [#Arguments [#Int '7'][#Infix left: [#Name 'c']name: [#Name '//']right: [#Name 'a']]]]],)
[[#Name 'x'], [#ApplyExpr name: [#Name 'min']params: [#Arguments [#Int '7'][#Infix left: [#Name 'c']name: [#Name '//']right: [#Name 'a']]]]]
# cをaで割った余り、かつ{{cをaで割った商}}が7より小さいとき、
if c % a and c//a < 7 :
  # ([[#Name 'x'], [#Int '1']],)
  [[#Name 'x'], [#Int '1']]
# xを出力する
print(x)
# '0から1000未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1000) :
  # "Hello World"を出力する
  print("Hello World")
# '0から4未満までの数列の各要素を順にiとして、繰り返す
for i  in range(4) :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にtとnとする
  t,n  = map(int,input().split())
  # 0をxとする
  x = 0
  # tが1のとき、
  if t == 1 :
    # 6000にnを掛けた値をxとする
    x = 6000*n
  # ('tが2の',)
  elif t == 2 :
    # 4000にnを掛けた値をxとする
    x = 4000*n
  # ('tが3の',)
  elif t == 3 :
    # 3000にnを掛けた値をxとする
    x = 3000*n
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'x']expr: [#Infix left: [#Int '2000']name: [#Name '*']right: [#Name 'n']]]]]
  # xを出力する
  print(x)
# '0から7未満までの数列の各要素を順にiとして、繰り返す
for i  in range(7) :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
  a,b  = map(int,input().split())
  # aからbを引いた値を出力する
  print(a-b)
# '0から9未満までの数列の各要素を順にiとして、繰り返す
for i  in range(9) :
  # '入力された文字列を空白で分割した列のリストを展開し順にn、a、bとする
  n,a,b  = list(input().split())
  # aの整数値にbの整数値を加えた値をxとする
  x = int(a) + int(b)
  # aの整数値に200を掛けた値にbの整数値に300を掛けた値を加えた値をyとする
  y = int(a)*200 + int(b)*300
  # [#Format [#Name 'n'][#StringPart ' '][#Name 'x'][#StringPart ' '][#Name 'y']]を出力する
  print(f"{n} {x} {y}")
# {{'0から10未満までの数列}}の各要素をiとし、入力された文字列の整数値の列をxとする
x = [int(input()) for i in range(10)]
# xの総和を出力する
print(sum(x))
# 1をiとする
i = 1
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をxとする
  x = int(input())
  # xが0のとき、
  if x == 0 :
    # 繰り返すのを中断する
    break
  # "Case"、iの文字列に":"を加えた値、xの文字列を出力する
  print("Case",str(i)+":",str(x))
  # ([[#Name 'i'], [#Int '1']],)
  [[#Name 'i'], [#Int '1']]
# 1の間、繰り返す
while 1 :
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
  a = list(map(int,input().split()))
  # a(0)がa(1)かどうかが0のとき、
  if a[0] == a[1] == 0 :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#Expression [#MethodExpr recv: [#Name 'a']name: [#Name 'sort']params: [#Arguments '']]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Format [#IndexExpr recv: [#Name 'a']index: [#Int '0']][#StringPart ' '][#IndexExpr recv: [#Name 'a']index: [#Int '1']]]]]]]]
# 入力された文字列の整数値をNとする
N = int(input())
# '0からN未満までの数列の各要素を順にiとして、繰り返す
for i  in range(N) :
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
  a = list(map(int,input().split()))
  # a.sort()
  a.sort()
  # aの最初値の2乗にa(1)の2乗を加えた値がa(2)の2乗のとき、
  if a[0]**2 +a[1]**2 == a[2]**2 :
    # "YES"を出力する
    print("YES")
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"NO"']]]]]]
# mathモジュールを用いる
import math
# 入力された文字列の整数値をnとする
n = int(input())
# 100000をxとする
x = 100000
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # ([[#Name 'x'], [#Double '1.05']],)
  [[#Name 'x'], [#Double '1.05']]
  # math.ceil(x)をxとする
  x = math.ceil(x)
  # xを1000で割った余りのとき、
  if x % 1000 :
    # xから({{xを1000で割った余り}})の組を引いた値に1000を加えた値をxとする
    x = x - (x % 1000) + 1000
# xを出力する
print(x)
# 1の間、繰り返す
while 1 :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'change']expr: [#Infix left: [#Int '1000']name: [#Name '-']right: [#Name 'n']]][#VarDecl name: [#Name 'sum_coin']expr: [#Int '0']][#VarDecl name: [#Name 'coin']expr: [#List [#Int '500'][#Int '100'][#Int '50'][#Int '10'][#Int '5'][#Int '1']]][#For each: [# [#Name 'i']]list: [#Name 'coin']body: [#Block [#VarDecl name: [#Name 'r']expr: [#Infix left: [#Name 'change']name: [#Name '//']right: [#Name 'i']]][#SelfAssignment left: [#Name 'change']name: [# '%=']right: [#Name 'i']][#SelfAssignment left: [#Name 'sum_coin']name: [# '+=']right: [#Name 'r']]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'sum_coin']]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a,b,c  = map(int,input().split())
# 0をxとする
x = 0
# 'aからbに1を加えた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(a,b+1) :
  # cをiで割った余りが0のとき、
  if c % i == 0 :
    # ([[#Name 'x'], [#Int '1']],)
    [[#Name 'x'], [#Int '1']]
  # ()
  else :[#Else [#Block [#Pass 'pass']]]
# xを出力する
print(x)
# '1から10未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1,10) :
  # '1から10未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(1,10) :
    # iにjを掛けた値をaとする
    a = i*j
    # "%dx%d=%d"を(i、j、a)の組で割った余りを出力する
    print("%dx%d=%d"%(i,j,a))
# 1の間、繰り返す
while 1 :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にWとHとする
  W,H = map(int,input().split())
  # WがHかどうかが0のとき、
  if W == H == 0 :
    # 繰り返すのを中断する
    break
  # '0からW未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(W) :
    # '0からH未満までの数列の各要素を順にjとして、繰り返す
    for j  in range(H) :
      # '#'と((end, ''))からなる辞書を出力する
      print('#',end='')
    # 空行を出力する
    print()
  # 空行を出力する
  print()
# 1の間、繰り返す
while 1 :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にHとWとする
  H,W  = map(int,input().split())
  # HがWかどうかが0のとき、
  if H == W == 0 :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'H']]]body: [#Block [#For each: [# [#Name 'j']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'W']]]body: [#Block [#If cond: [#Or left: [#Infix left: [#Name 'i']name: [#Name '==']right: [#Int '0']]right: [#Infix left: [#Name 'j']name: [#Name '==']right: [#Int '0']]]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"#"'][#Data [#KeyValue name: [#Name 'end']value: [#QString "''"]]]]]]]elif: [# [#Elif cond: [#Or left: [#Infix left: [#Name 'i']name: [#Name '==']right: [#Infix left: [#Name 'H']name: [#Name '-']right: [#Int '1']]]right: [#Infix left: [#Name 'j']name: [#Name '==']right: [#Infix left: [#Name 'W']name: [#Name '-']right: [#Int '1']]]]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"#"'][#Data [#KeyValue name: [#Name 'end']value: [#QString "''"]]]]]]]]]else: [#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"."'][#Data [#KeyValue name: [#Name 'end']value: [#QString "''"]]]]]]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments '']]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments '']]]]]
# 1の間、繰り返す
while 1 :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にHとWとする
  H,W  = map(int,input().split())
  # HがWかどうかが0のとき、
  if H == W == 0 :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'H']]]body: [#Block [#For each: [# [#Name 'j']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'W']]]body: [#Block [#If cond: [#Infix left: [#Infix left: [#Tuple [#Infix left: [#Name 'i']name: [#Name '+']right: [#Name 'j']]]name: [#Name '%']right: [#Int '2']]name: [#Name '==']right: [#Int '0']]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"#"'][#Data [#KeyValue name: [#Name 'end']value: [#QString "''"]]]]]]]else: [#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"."'][#Data [#KeyValue name: [#Name 'end']value: [#QString "''"]]]]]]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments '']]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments '']]]]]
# 1の間、繰り返す
while 1 :
  # 入力された文字列を空白で分割した列を展開し順にa、op、bとする
  a,op,b  = input().split()
  # aの整数値をaとする
  a = int(a)
  # bの整数値をbとする
  b = int(b)
  # opが"?"のとき、
  if op == "?" :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#If cond: [#Infix left: [#Name 'op']name: [#Name '==']right: [#QString '"+"']]then: [#Block [#VarDecl name: [#Name 'x']expr: [#Infix left: [#Name 'a']name: [#Name '+']right: [#Name 'b']]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'x']]]]]elif: [# [#Elif cond: [#Infix left: [#Name 'op']name: [#Name '==']right: [#QString '"-"']]then: [#Block [#VarDecl name: [#Name 'x']expr: [#Infix left: [#Name 'a']name: [#Name '-']right: [#Name 'b']]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'x']]]]]][#Elif cond: [#Infix left: [#Name 'op']name: [#Name '==']right: [#QString '"*"']]then: [#Block [#VarDecl name: [#Name 'x']expr: [#Infix left: [#Name 'a']name: [#Name '*']right: [#Name 'b']]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'x']]]]]][#Elif cond: [#Infix left: [#Name 'op']name: [#Name '==']right: [#QString '"/"']]then: [#Block [#VarDecl name: [#Name 'x']expr: [#Infix left: [#Name 'a']name: [#Name '//']right: [#Name 'b']]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'x']]]]]]]else: [#Else [#Block [#Pass 'pass']]]]]]
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# a.sort()
a.sort()
# [#Format [#IndexExpr recv: [#Name 'a']index: [#Int '0']][#StringPart ' '][#IndexExpr recv: [#Name 'a']index: [#Infix left: [#Name 'n']name: [#Name '-']right: [#Int '1']]][#StringPart ' '][#ApplyExpr name: [#Name 'sum']params: [#Arguments [#Name 'a']]]]を出力する
print(f"{a[0]} {a[n-1]} {sum(a)}")
# 1の間、繰り返す
while 1 :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # {{'0からn未満までの数列}}の各要素をiとし、入力された文字列の整数値の列をsとする
  s = [int(input()) for i in range(n)]
  # s.sort()
  s.sort()
  # sの総和から({{s(0)にsの末尾値を加えた値}})の組を引いた値をxとする
  x = sum(s) - (s[0] + s[-1])
  # xを({{nから2を引いた値}})の組で割った商を出力する
  print(x // (n - 2))
# mathモジュールを用いる
import math
# 1の間、繰り返す
while 1 :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # 0をiとする
  i = 0
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # math.factorial(n)の文字列の逆順をnとする
  n = str(math.factorial(n))[::-1]
  # n(i)が'0'の間、繰り返す
  while n[i]=='0' :
    # ([[#Name 'i'], [#Int '1']],)
    [[#Name 'i'], [#Int '1']]
  # iを出力する
  print(i)   
Syntax Error ((unknown source):25:14+573)
  print(f'{s.x:,.8f} {s.y:,.8f}')
              ^                  
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# a.reverse()
a.reverse()
# *(a)を出力する
print(*a)
# 0をcとする
c = 0
# '0から5未満までの数列の各要素を順にiとして、繰り返す
for i  in range(5) :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが40より小さいとき、
  if n < 40 :
    # 40をnとする
    n = 40
  # ([[#Name 'c'], [#Name 'n']],)
  [[#Name 'c'], [#Name 'n']]
# cを5で割った商を出力する
print(c // 5)
# 空列をaとする
a = []
# 空列をbとする
b = []
# '0から4未満までの数列の各要素を順にiとして、繰り返す
for i  in range(4) :
  # a.append(int(input()))
  a.append(int(input()))
  # a.sort(reverse=True)
  a.sort(reverse=True)
# '4から6未満までの数列の各要素を順にjとして、繰り返す
for j  in range(4,6) :
  # b.append(int(input()))
  b.append(int(input()))
  # b.sort(reverse=True)
  b.sort(reverse=True)
# {{aの位置先頭から位置3までの部分}}の総和にbの最初値を加えた値を出力する
print(sum(a[:3])+b[0])
# 空列をaとする
a = []
# 空列をbとする
b = []
# '0から10未満までの数列の各要素を順にiとして、繰り返す
for i  in range(10) :
  # a.append(int(input()))
  a.append(int(input()))
  # a.sort()
  a.sort()
# aの先頭7個を取り除いた部分の総和をWとする
W = sum(a[7:])
# '10から20未満までの数列の各要素を順にjとして、繰り返す
for j  in range(10,20) :
  # b.append(int(input()))
  b.append(int(input()))
  # b.sort()
  b.sort()
# bの先頭7個を取り除いた部分の総和をKとする
K = sum(b[7:])
# [#Format [#Name 'W'][#StringPart ' '][#Name 'K']]を出力する
print(f'{W} {K}')
# '{{'0から31未満までの数列}}の先頭を除いた部分のリストをnとする
n = list(range(31)[1:])
# '0から28未満までの数列の各要素を順にiとして、繰り返す
for i  in range(28) :
  # nから入力された文字列の整数値を取り除いた集まり
  n.remove(int(input()))
# nの最初値を出力する
print(n[0])
# n(1)を出力する
print(n[1])
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをxとする
x = list(map(int,input().split()))
# xの最大値からxの最小値を引いた値の絶対値をmとする
m = abs(max(x) - min(x))
# mを2で割った余りのとき、
if m % 2 :
  # mに1を加えた値をmとする
  m = m + 1
  # mを2で割った商を出力する
  print(m // 2)
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Infix left: [#Name 'm']name: [#Name '//']right: [#Int '2']]]]]]]
# 1の間、繰り返す
while 1 :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にnとkとする
  n,k  = map(int,input().split())
  # nがkかどうかが0のとき、
  if n == k == 0 :
    # 繰り返すのを中断する
    break
  # 空列をaとする
  a = []
  # '0からn未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(n) :
    # a.append(int(input()))
    a.append(int(input()))
    # 0をcとする
    c = 0
  # '0からk未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(k) :
    # ([[#Name 'c'], [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]],)
    [[#Name 'c'], [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]]
    # cをbとする
    b = c
  # 'kからn未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(k, n) :
    # ([[#Name 'c'], [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]],)
    [[#Name 'c'], [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]]
    # ([[#Name 'c'], [#IndexExpr recv: [#Name 'a']index: [#Infix left: [#Name 'i']name: [#Name '-']right: [#Name 'k']]]],)
    [[#Name 'c'], [#IndexExpr recv: [#Name 'a']index: [#Infix left: [#Name 'i']name: [#Name '-']right: [#Name 'k']]]]
    # bとcの最大値をbとする
    b = max(b,c)
  # bを出力する
  print(b)
# {{'0から10未満までの数列}}の各要素をiとし、入力された文字列の整数値の列をxとする
x = [int(input()) for i in range(10)]
# x.sort(reverse=True)
x.sort(reverse=True)
# '0から3未満までの数列の各要素を順にiとして、繰り返す
for i  in range(3) :
  # x(i)を出力する
  print(x[i])
# 1の間、繰り返す
while 1 :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # {{'0から10未満までの数列}}の各要素をiとし、0の列をxとする
  x = [0 for i in range(10)] 
  # '0からn未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(n) :
    # 入力された文字列の整数値をcとする
    c = int(input())
    # ([[#IndexExpr recv: [#Name 'x']index: [#Name 'c']], [#Int '1']],)
    [[#IndexExpr recv: [#Name 'x']index: [#Name 'c']], [#Int '1']]
  # '0から10未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(10) :
    # '*'にx(i)を掛けた値をcountとする
    count = '*' * x[i] 
    # countの長さが0のとき、
    if len(count) == 0 :
      # "-"を出力する
      print("-")
    # ()
    else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'count']]]]]]
# 入力された文字列をxとする
x = input()
# xを英大文字に変換した文字列を出力する
print(x.upper())
# 入力された文字列をxとする
x = input()
# xの英大文字を英小文字、英小文字を英大文字に変換した文字列を出力する
print(x.swapcase())
# sysモジュールを用いる
import sys
# 空辞書をxとする
x = {}
# sys.stdinの各要素を順にlineとして、繰り返す
for line  in sys.stdin :
  # lineの各要素を順にlとして、繰り返す
  for l  in line :
    # lが全てアルファベットのとき、
    if l.isalpha() :
      # lを英小文字に変換した文字列をcとする
      c = l.lower()
      # x.get(c,0)に1を加えた値をx[c] にする
      x[c]  = x.get(c,0)+1
# '0から26未満までの数列の各要素を順にiとして、繰り返す
for i  in range(26) :
  # 文字コード'a'の順序数にiを加えた値の文字をcとする
  c = chr(ord('a')+i)
  # [#Format [#Name 'c'][#StringPart ' : '][#MethodExpr recv: [#Name 'x']name: [#Name 'get']params: [#Arguments [#Name 'c'][#Int '0']]]]を出力する
  print(f'{c} : {x.get(c,0)}')
# 1の間、繰り返す
while 1 :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # 'nの文字列のリストの各要素をiとし、iの整数値の列をxとする
  x = [int(i) for i in list(str(n))]
  # xの総和を出力する
  print(sum(x))
# 入力された文字列をnとする
n = input()
# {{n内の"K"の出現をカウントした整数}}、{{n内の"U"の出現をカウントした整数}}、{{n内の"P"の出現をカウントした整数}}、{{n内の"C"の出現をカウントした整数}}の最小値を出力する
print(min(n.count("K"),n.count("U"),n.count("P"),n.count("C")))
# 入力された文字列をWとする
W = input()
# 0をxとする
x = 0
# 1の間、繰り返す
while 1 :
  # 入力された文字列をTとする
  T = input()
  # Tが'END_OF_TEXT'のとき、
  if T == 'END_OF_TEXT' :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 'x']name: [# '+=']right: [#MethodExpr recv: [#MethodExpr recv: [#MethodExpr recv: [#Name 'T']name: [#Name 'lower']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]name: [#Name 'count']params: [#Arguments [#Name 'W']]]]]]
# xを出力する
print(x)
# 入力された文字列をsとする
s = input()
# 入力された文字列をpとする
p = input()
# pがsに2を掛けた値に含まれるとき、
if p in s*2 :
  # "Yes"を出力する
  print("Yes")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"No"']]]]]]
# 入力された文字列をtとする
t = input()
# 入力された文字列をpとする
p = input()
# '0から{{tの長さからpの長さを引いた値}}に1を加えた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(t) - len(p) + 1) :
  # tの位置iから位置{{iにpの長さを加えた値}}までの部分がpのとき、
  if t[i:i + len(p)] == p :
    # iを出力する
    print(i)
  # ()
  else :[#Else [#Block [#Pass 'pass']]]
# 1の間、繰り返す
while 1 :
  # 入力された文字列をnとする
  n = input()
  # nが"-"のとき、
  if n == "-" :
    # 繰り返すのを中断する
    break
  # 入力された文字列の整数値をmとする
  m = int(input())
  # '0からm未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(m) :
    # 入力された文字列の整数値をhとする
    h = int(input())
    # nの先頭h個を取り除いた部分にnの位置先頭から位置hまでの部分を加えた値をnとする
    n = n[h:] + n[:h]
  # nを出力する
  print(n)
# 入力された文字列の整数値をnとする
n = int(input())
# 0をaとする
a = 0
# 0をbとする
b = 0
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # map(str,入力された文字列を空白で分割した列)を展開し順にAとBとする
  A,B = map(str,input().split())
  # AがBより大きいとき、
  if A > B  :
    # ([[#Name 'a'], [#Int '3']],)
    [[#Name 'a'], [#Int '3']]
  # AがBより小さいとき、
  if A < B  :
    # ([[#Name 'b'], [#Int '3']],)
    [[#Name 'b'], [#Int '3']]
  # AがBのとき、
  if A == B  :
    # ([[#Name 'a'], [#Int '1']],)
    [[#Name 'a'], [#Int '1']]
    # ([[#Name 'b'], [#Int '1']],)
    [[#Name 'b'], [#Int '1']]
# aとbを出力する
print(a,b)
# 1の間、繰り返す
while 1 :
  # 入力された文字列をxとする
  x = input()
  # xが"0"のとき、
  if x == "0" :
    # 繰り返すのを中断する
    break
  # 0をaとする
  a = 0
  # 0をbとする
  b = 0
  # '1からxの長さ未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(1,len(x)) :
    # x(i)が"A"のとき、
    if x[i] == "A" :
      # ([[#Name 'a'], [#Int '1']],)
      [[#Name 'a'], [#Int '1']]
    # ()
    else :[#Else [#Block [#SelfAssignment left: [#Name 'b']name: [# '+=']right: [#Int '1']]]]
  # aがbより大きいとき、
  if a > b :
    # ([[#Name 'a'], [#Int '1']],)
    [[#Name 'a'], [#Int '1']]
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 'b']name: [# '+=']right: [#Int '1']]]]
  # aとbを出力する
  print(a,b)    
# mathモジュールを用いる
import math
# map(float,入力された文字列を空白で分割した列)を展開し順にx1、y1、x2、y2とする
x1,y1,x2,y2  = map(float,input().split())
# math.sqrt((x1 - x2)**2 + (y1-y2)**2)をdとする
d = math.sqrt((x1 - x2)**2 + (y1-y2)**2)
# format(d)を出力する
print('{:.8f}'.format(d))
# mathモジュールを用いる
import math
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a,b,c  = map(int,input().split())
# ({{math.piを180で割った値}})の組にcを掛けた値をthとする
th = (math.pi/180)*c
# {{{{1を2で割った値}}にaを掛けた値}}にbを掛けた値にmath.sin(th)を掛けた値をsとする
s = 1/2 * a * b * math.sin(th)
# math.sqrt(a**2 + b**2 - 2*a*b*math.cos(th))をc2とする
c2 = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(th))
# aにbを加えた値にc2を加えた値をlとする
l = a + b + c2
# 2にsを掛けた値をaで割った値をhとする
h = 2 * s / a
# format(s)を出力する
print('{:.8f}'.format(s))
# format(l)を出力する
print('{:.8f}'.format(l))
# format(h)を出力する
print('{:.8f}'.format(h))
# statisticsモジュールを用いる
import statistics
# 1の間、繰り返す
while 1 :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをsとする
  s = list(map(int, input().split()))
  # statistics.pstdev(s)をxとする
  x = statistics.pstdev(s)
  # format(x)を出力する
  print('{:.8f}'.format(x))
# 1の間、繰り返す
while 1 :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にm、f、rとする
  m,f,r  = map(int,input().split())
  # mにfを加えた値をpとする
  p = m + f 
  # {{mがfかどうか}}がrかどうかが-1のとき、
  if m == f == r == -1 :
    # 繰り返すのを中断する
    break
  # mが-1、またはfが-1のとき、
  if m == -1 or f == -1 :
    # "F"を出力する
    print("F")
  # ('pが80以上の',)
  elif p >= 80 :
    # "A"を出力する
    print("A")
  # ('65がp以下かどうかが80より小さい',)
  elif 65 <= p < 80 :
    # "B"を出力する
    print("B")
  # ('50がp以下かどうかが65より小さい',)
  elif 50 <= p < 65 :
    # "C"を出力する
    print("C")
  # ('30がp以下かどうかが50より小さい',)
  elif 30 <= p < 50 :
    # rが50以上のとき、
    if r >= 50 :
      # "C"を出力する
      print("C")
    # ()
    else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"D"']]]]]]
  # ('pが30より小さい',)
  elif p < 30 :
    # "F"を出力する
    print("F")
  # ()
  else :[#Else [#Block [#Pass 'pass']]]
# 1の間、繰り返す
while 1 :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にnとxとする
  n,x  = map(int,input().split())
  # 0をcとする
  c = 0
  # nがxかどうかが0のとき、
  if n == x == 0 :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '1'][#Infix left: [#Name 'n']name: [#Name '+']right: [#Int '1']]]]body: [#Block [#For each: [# [#Name 'j']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'i'][#Infix left: [#Name 'n']name: [#Name '+']right: [#Int '1']]]]body: [#Block [#For each: [# [#Name 'k']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'j'][#Infix left: [#Name 'n']name: [#Name '+']right: [#Int '1']]]]body: [#Block [#If cond: [#Or left: [#Or left: [#Infix left: [#Name 'i']name: [#Name '==']right: [#Name 'j']]right: [#Infix left: [#Name 'i']name: [#Name '==']right: [#Name 'k']]]right: [#Infix left: [#Name 'j']name: [#Name '==']right: [#Name 'k']]]then: [#Block [#Pass 'pass']]elif: [# [#Elif cond: [#Infix left: [#Infix left: [#Infix left: [#Name 'i']name: [#Name '+']right: [#Name 'j']]name: [#Name '+']right: [#Name 'k']]name: [#Name '==']right: [#Name 'x']]then: [#Block [#SelfAssignment left: [#Name 'c']name: [# '+=']right: [#Int '1']]]]]else: [#Else [#Block [#Pass 'pass']]]]]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'c']]]]]]
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストを展開し順にnとmとする
n, m  = list(map(int, input().split()))
# 空列をaとする
a = []
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # a.append([int(j) for j in input().split()])
  a.append([int(j) for j in input().split()])
# 空列をbとする
b = []
# '0からm未満までの数列の各要素を順にiとして、繰り返す
for i  in range(m) :
  # b.append(int(input()))
  b.append(int(input()))
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # 0をsとする
  s = 0
  # '0からm未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(m) :
    # ([[#Name 's'], [#Infix left: [#IndexExpr recv: [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]index: [#Name 'j']]name: [#Name '*']right: [#IndexExpr recv: [#Name 'b']index: [#Name 'j']]]],)
    [[#Name 's'], [#Infix left: [#IndexExpr recv: [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]index: [#Name 'j']]name: [#Name '*']right: [#IndexExpr recv: [#Name 'b']index: [#Name 'j']]]]
  # sを出力する
  print(s)
# map(整数,入力された文字列を空白で分割した列)を展開し順にn、m、lとする
n,m,l   = map(int, input().split())
# 空列をaとする
a = []
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # a.append(list(map(int,input().split())))
  a.append(list(map(int,input().split())))
# 空列をbとする
b = []
# '0からm未満までの数列の各要素を順にiとして、繰り返す
for i  in range(m) :
  # b.append(list(map(int,input().split())))
  b.append(list(map(int,input().split())))
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # 空列をxとする
  x = []
  # '0からl未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(l) :
    # 0をsとする
    s = 0
    # '0からm未満までの数列の各要素を順にkとして、繰り返す
    for k  in range(m) :
      # ([[#Name 's'], [#Infix left: [#IndexExpr recv: [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]index: [#Name 'k']]name: [#Name '*']right: [#IndexExpr recv: [#IndexExpr recv: [#Name 'b']index: [#Name 'k']]index: [#Name 'j']]]],)
      [[#Name 's'], [#Infix left: [#IndexExpr recv: [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]index: [#Name 'k']]name: [#Name '*']right: [#IndexExpr recv: [#IndexExpr recv: [#Name 'b']index: [#Name 'k']]index: [#Name 'j']]]]
    # x.append(s)
    x.append(s)
  # 'map(str,x)のリストを文字列" "で連結した文字列を出力する
  print(" ".join(list(map(str, x))))
# map(整数,入力された文字列を空白で分割した列)を展開し順にrとcとする
r,c  = map(int,input().split())
# 空列をaとする
a = []
# '0からr未満までの数列の各要素を順にiとして、繰り返す
for i  in range(r) :
  # a.append(list(map(int, input().split())))
  a.append(list(map(int, input().split())))
  # ([[#IndexExpr recv: [#Name 'a']index: [#Name 'i']], [#List [#ApplyExpr name: [#Name 'sum']params: [#Arguments [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]]]]],)
  [[#IndexExpr recv: [#Name 'a']index: [#Name 'i']], [#List [#ApplyExpr name: [#Name 'sum']params: [#Arguments [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]]]]]
  # *(a(i))を出力する
  print(*a[i])
# '*(aの逆順)の要素をそれぞれ組にした列のリストをaとする
a = list(zip(*a[::-1]))
# '0からc未満までの数列の各要素を順にiとして、繰り返す
for i  in range(c) :
  # a(i)の総和と((end, ' '))からなる辞書を出力する
  print(sum(a[i]),end=' ')
# a(c)の総和を出力する
print(sum(a[c]))
# 入力された文字列の整数値をnとする
n = int(input())
# nをn1とする
n1 = n
# 2をiとする
i = 2
# 空列をxとする
x = []
# iにiを掛けた値がn以下の間、繰り返す
while i*i <= n :
  # nをiで割った余りが0の間、繰り返す
  while n % i == 0 :
    # ([[#Name 'n'], [#Name 'i']],)
    [[#Name 'n'], [#Name 'i']]
    # x.append(str(i))
    x.append(str(i))
  # ([[#Name 'i'], [#Int '1']],)
  [[#Name 'i'], [#Int '1']]
# nが1より大きいとき、
if n > 1 :
  # x.append(str(n))
  x.append(str(n))
# {{n1の文字列に": "を加えた値}}に{{xを文字列" "で連結した文字列}}を加えた値を出力する
print(str(n1) + ": " + " ".join(x))
# 1000000007をxとする
x = 1000000007
# map(整数,入力された文字列を空白で分割した列)を展開し順にmとnとする
m,n = map(int,input().split())
# mのn乗に対するxの剰余を出力する
print(pow(m,n,x))
# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def gcd (a,b) :
  # 0をcとする
  c = 0
  # bが0と等しくない間、繰り返す
  while b != 0 :
    # bとaをbで割った余りをaとbとする
    a,b  = b,a % b
    # ([[#Name 'c'], [#Int '1']],)
    [[#Name 'c'], [#Int '1']]
  # (aとc)からなる列を関数出力とする
  return [a,c]
# 1の間、繰り返す
while 1 :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
  x,y  = map(int,input().split())
  # xが0のとき、
  if x == 0 :
    # 繰り返すのを中断する
    break
  # xとyの最大値とxとyの最小値をxとyとする
  x,y  = max(x,y),min(x,y)
  # *((gcd(x,y))の組)を出力する
  print(*(gcd(x,y)))
# fractionsモジュールを用いる
import fractions
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int, input().split()))
# aの最初値をxとする
x = a[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1, n) :
  # xにa(i)を掛けた値をfractions.gcd(x, a[i])で割った商をxとする
  x = x * a[i] // fractions.gcd(x, a[i])
# xを出力する
print(x)
# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def gcd (a,b) :
  # bが0と等しくない間、繰り返す
  while b != 0 :
    # bとaをbで割った余りをaとbとする
    a,b  = b,a % b
  # aを関数出力とする
  return a
# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x,y  = map(int,input().split())    
# xとyの最大値とxとyの最小値をxとyとする
x,y  = max(x,y),min(x,y)
# gcd(x,y)を出力する
print(gcd(x,y))
# mathモジュールを用いる
import math
# 関数primeを[#FuncParam [#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def prime (n) :
  # nが1以下のとき、
  if n <= 1 :
    # 偽を関数出力とする
    return False
  # '2からm.sqrt(n)の整数値に1を加えた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(2,int(m.sqrt(n)) + 1) :
    # nをiで割った余りが0のとき、
    if n % i == 0 :
      # 偽を関数出力とする
      return False
  # 真を関数出力とする
  return True
# 入力された文字列の整数値をaとする
a = int(input())
# 空列をxとする
x = []
# '0からa未満までの数列の各要素を順にjとして、繰り返す
for j  in range(a) :
  # 入力された文字列の整数値をbとする
  b = int(input())
  # prime(b)のとき、
  if prime(b) :
    # x.append(b)
    x.append(b)
# xの長さを出力する
print(len(x))
# mathモジュールを用いる
import math
# 関数primeを[#FuncParam [#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def prime (n) :
  # nが1以下のとき、
  if n <= 1 :
    # 偽を関数出力とする
    return False
  # '2からm.sqrt(n)の整数値に1を加えた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(2,int(m.sqrt(n)) + 1) :
    # nをiで割った余りが0のとき、
    if n % i == 0 :
      # 偽を関数出力とする
      return False
  # 真を関数出力とする
  return True
# 関数Goldbachを[#FuncParam [#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def Goldbach (n) :
  # 空列をxとする
  x = []
  # 0をcとする
  c = 0
  # '0からnに1を加えた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(n+1) :
    # prime(i)のとき、
    if prime(i) :
      # x.append(i)
      x.append(i)
  # xの各要素を順にjとして、繰り返す
  for j  in x :
    # xの各要素を順にkとして、繰り返す
    for k  in x :
      # jがkより大きいとき、
      if j > k :
        # 何もしない
        pass
      # ('jにkを加えた値がnの',)
      elif j + k == n :
        # ([[#Name 'c'], [#Int '1']],)
        [[#Name 'c'], [#Int '1']]
      # ()
      else :[#Else [#Block [#Pass 'pass']]]
  # cを出力する
  print(c)
# 1の間、繰り返す
while 1 :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # Goldbach(n)
  Goldbach(n)
# 関数collatzを[#FuncParam [#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def collatz (n) :
  # 0をcとする
  c = 0
  # nが1より大きい間、繰り返す
  while n > 1 :
    # nを2で割った余りが0のとき、
    if n % 2 == 0 :
      # nを2で割った値をnとする
      n = n / 2
      # ([[#Name 'c'], [#Int '1']],)
      [[#Name 'c'], [#Int '1']]
    # ()
    else :[#Else [#Block [#VarDecl name: [#Name 'n']expr: [#Infix left: [#Infix left: [#Name 'n']name: [#Name '*']right: [#Int '3']]name: [#Name '+']right: [#Int '1']]][#SelfAssignment left: [#Name 'c']name: [# '+=']right: [#Int '1']]]]
  # cを関数出力とする
  return c
# 1の間、繰り返す
while 1 :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#ApplyExpr name: [#Name 'collatz']params: [#Arguments [#Name 'n']]]]]]]]
# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 'd']expr: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]]]except: [# [#Except body: [#Block [#Break 'break']]]]]
  # 0をcとする
  c = 0
  # dをxとする
  x = d
  # xが600より小さい間、繰り返す
  while x < 600 :
    # ([[#Name 'c'], [#Infix left: [#Tuple [#Infix left: [#Name 'x']name: [#Name '**']right: [#Int '2']]]name: [#Name '*']right: [#Name 'd']]],)
    [[#Name 'c'], [#Infix left: [#Tuple [#Infix left: [#Name 'x']name: [#Name '**']right: [#Int '2']]]name: [#Name '*']right: [#Name 'd']]]
    # ([[#Name 'x'], [#Name 'd']],)
    [[#Name 'x'], [#Name 'd']]
  # cを出力する
  print(c)
Syntax Error ((unknown source):6:18+141)
        print(f'{x:.3f} {y:.3f}')
                  ^              
# 入力された文字列をaとする
a = input()
# a内の"."を" "で置き換えた文字列をaとする
a = a.replace("."," ")
# a内の","を" "で置き換えた文字列をaとする
a = a.replace(","," ")
# aを空白で分割した列をxとする
x = a.split()
# 空列をyとする
y = []
# '0からxの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(x)) :
  # 3がx(i)の長さ以下かどうかが6以下のとき、
  if 3 <= len(x[i]) <= 6 :
    # y.append(x[i])
    y.append(x[i])
# yを文字列" "で連結した文字列を出力する
print(" ".join(y))
# 入力された文字列をstrとする
str = input()
# strの逆順を出力する
print(str[::-1])
# 1の間、繰り返す
while 1 :
  # 入力された文字列をaとする
  a = input()
  # aが"END OF INPUT"のとき、
  if a == "END OF INPUT" :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'c']expr: [#Int '0']][#For each: [# [#Name 'i']]list: [#Name 'a']body: [#Block [#If cond: [#Infix left: [#Name 'i']name: [#Name '==']right: [#QString "' '"]]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'c'][#Data [#KeyValue name: [#Name 'end']value: [#QString '""']]]]]][#VarDecl name: [#Name 'c']expr: [#Int '0']]]else: [#Else [#Block [#SelfAssignment left: [#Name 'c']name: [# '+=']right: [#Int '1']]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'c']]]]]]
# 1の間、繰り返す
while 1 :[#Try body: [#Block [#VarDecl name: [#Name 'a']expr: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]except: [# [#Except body: [#Block [#Break 'break']]]]]
  # 0をbとする
  b = 0
  # 0をcとする
  c = 0
  # '0からaの長さから2を引いた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(len(a)-2) :
    # aの位置iから位置{{iに3を加えた値}}までの部分が'JOI'のとき、
    if a[i:i+3]=='JOI' :
      # ([[#Name 'b'], [#Int '1']],)
      [[#Name 'b'], [#Int '1']]
    # ("aの位置iから位置{{iに3を加えた値}}までの部分が'IOI'の",)
    elif a[i:i+3]=='IOI' :
      # ([[#Name 'c'], [#Int '1']],)
      [[#Name 'c'], [#Int '1']]
    # ()
    else :[#Else [#Block [#Pass 'pass']]]
  # bを出力する
  print(b)
  # cを出力する
  print(c)
# 0をaとする
a = 0
# 1の間、繰り返す
while 1 :[#Try body: [#Block [#VarDecl name: [#Name 'n']expr: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]][#If cond: [#Infix left: [#Name 'n']name: [#Name '==']right: [#SliceExpr recv: [#Name 'n']step: [#Unary name: [#Name '-']expr: [#Int '1']]]]then: [#Block [#SelfAssignment left: [#Name 'a']name: [# '+=']right: [#Int '1']]]]]except: [# [#Except body: [#Block [#Break 'break']]]]]
# aを出力する
print(a)
# 関数derot_nを[#FuncParam [#ParamDecl name: [#Name 's']][#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def derot_n (s, n) :
  # ''をansとする
  ans = ''
  # sの各要素を順にletterとして、繰り返す
  for letter  in s :
    # ([[#Name 'ans'], [#ApplyExpr name: [#Name 'chr']params: [#Arguments [#Infix left: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#QString "'Z'"]]]name: [#Name '-']right: [#Infix left: [#Tuple [#Infix left: [#Infix left: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#QString "'Z'"]]]name: [#Name '-']right: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#Name 'letter']]]]name: [#Name '+']right: [#Name 'n']]]name: [#Name '%']right: [#Int '26']]]]]],)
    [[#Name 'ans'], [#ApplyExpr name: [#Name 'chr']params: [#Arguments [#Infix left: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#QString "'Z'"]]]name: [#Name '-']right: [#Infix left: [#Tuple [#Infix left: [#Infix left: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#QString "'Z'"]]]name: [#Name '-']right: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#Name 'letter']]]]name: [#Name '+']right: [#Name 'n']]]name: [#Name '%']right: [#Int '26']]]]]]
  # ansを関数出力とする
  return ans
# derot_n(入力された文字列,3)を出力する
print(derot_n(input(), 3))
# 入力された文字列を空白で分割した列をnとする
n = input().split()
# nと((key, nのcount))からなる辞書の最大値とnと((key, len))からなる辞書の最大値を出力する
print(max(n, key=n.count),max(n, key=len))
# 入力された文字列をnとする
n = input()
# n内の'apple'を'x'で置き換えた文字列をnとする
n = n.replace('apple','x')
# n内の'peach'を'apple'で置き換えた文字列をnとする
n = n.replace('peach','apple')
# n内の'x'を'peach'で置き換えた文字列をnとする
n = n.replace('x','peach')
# nを出力する
print(n)
# reモジュールを用いる
import re
# 0をaとする
a = 0
# 1の間、繰り返す
while 1 :[#Try body: [#Block [#VarDecl name: [#Name 'n']expr: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]except: [# [#Except body: [#Block [#Break 'break']]]]]
  # re.findall('[0-9]+',n)の各要素を順にiとして、繰り返す
  for i  in re.findall('[0-9]+',n) :
    # ([[#Name 'a'], [#ApplyExpr name: [#Name 'int']params: [#Arguments [#Name 'i']]]],)
    [[#Name 'a'], [#ApplyExpr name: [#Name 'int']params: [#Arguments [#Name 'i']]]]
# aを出力する
print(a)
# 1の間、繰り返す
while 1 :[#Try body: [#Block [#VarDecl name: [#Name 'a']expr: [#ApplyExpr name: [#Name 'list']params: [#Arguments [#ApplyExpr name: [#Name 'map']params: [#Arguments [#Name 'int'][#MethodExpr recv: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]]]]]][#VarDecl name: [#Name 'b']expr: [#ApplyExpr name: [#Name 'list']params: [#Arguments [#ApplyExpr name: [#Name 'map']params: [#Arguments [#Name 'int'][#MethodExpr recv: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]]]]]][#VarDecl name: [#Name 'hit']expr: [#Int '0']][#VarDecl name: [#Name 'blow']expr: [#Int '0']][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '4']]]body: [#Block [#If cond: [#Infix left: [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]name: [#Name '==']right: [#IndexExpr recv: [#Name 'b']index: [#Name 'i']]]then: [#Block [#SelfAssignment left: [#Name 'hit']name: [# '+=']right: [#Int '1']]]elif: [# [#Elif cond: [#Infix left: [#IndexExpr recv: [#Name 'b']index: [#Name 'i']]name: [#Name 'in']right: [#Name 'a']]then: [#Block [#SelfAssignment left: [#Name 'blow']name: [# '+=']right: [#Int '1']]]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'hit'][#Name 'blow']]]]]except: [# [#Except body: [#Block [#Break 'break']]]]]
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # 0をcとする
  c = 0
  # nが0のとき、
  if n==0 :
    # 繰り返すのを中断する
    break
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをnsとする
  ns = list(map(int, input().split()))
  # '0からn未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(n) :
    # ns(i)がnsの総和をnで割った値以下のとき、
    if ns[i]<=sum(ns)/n :
      # ([[#Name 'c'], [#Int '1']],)
      [[#Name 'c'], [#Int '1']]
  # cを出力する
  print(c)
# map(整数,入力された文字列を空白で分割した列)を展開し順にDとLとする
D,L = map(int,input().split())
# DをLで割った商をxとする
x = D//L
# DをLで割った余りが0のとき、
if D%L==0 :
  # xを出力する
  print(x)
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Infix left: [#Name 'x']name: [#Name '+']right: [#Tuple [#Infix left: [#Name 'D']name: [#Name '-']right: [#Infix left: [#Name 'L']name: [#Name '*']right: [#Name 'x']]]]]]]]]]
# 入力された文字列をsとする
s = input()
# {{len(s) が6より小さく}}、または{{sが全てアルファベットかどうか}}、または{{sが全て数字かどうか}}、または{{sの全てが英小文字かどうか}}、またはsの全てが英大文字のとき、
if len(s) < 6 or s.isalpha() or s.isdigit() or s.islower() or s.isupper() :
  # "INVALID"を出力する
  print("INVALID")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"VALID"']]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にH、a、bとする
H,a,b = map(int,input().split())
# 0をcとする
c = 0
# 'aからbに1を加えた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(a,b+1) :
  # Hをiで割った余りが0のとき、
  if H%i==0  :
    # ([[#Name 'c'], [#Int '1']],)
    [[#Name 'c'], [#Int '1']]
# cを出力する
print(c)
# 入力された文字列の整数値をnとする
n = int(input())
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
  a = list(map(int,input().split()))
  # 0をbとする
  b = 0
  # 0をcとする
  c = 0
  # 0をxとする
  x = 0
  # '0から10未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(10) :
    # bがa(j)より小さいとき、
    if b < a[j] :
      # a(j)をbとする
      b = a[j]
    # ('cがa(j)より小さい',)
    elif c < a[j] :
      # a(j)をcとする
      c = a[j]
    # ()
    else :[#Else [#Block [#SelfAssignment left: [#Name 'x']name: [# '+=']right: [#Int '1']]]]
  # xが0のとき、
  if x == 0 :
    # "YES"を出力する
    print("YES")
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"NO"']]]]]]
# 1の間、繰り返す
while 1 :[#Try body: [#Block [#VarDecl name: [#Name 'n']expr: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]][#VarDecl name: [#Name 'count']expr: [#Int '0']][#For each: [# [#Name 'a']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '10']]]body: [#Block [#For each: [# [#Name 'b']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '10']]]body: [#Block [#For each: [# [#Name 'c']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '10']]]body: [#Block [#For each: [# [#Name 'd']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '10']]]body: [#Block [#If cond: [#Infix left: [#Infix left: [#Infix left: [#Infix left: [#Name 'a']name: [#Name '+']right: [#Name 'b']]name: [#Name '+']right: [#Name 'c']]name: [#Name '+']right: [#Name 'd']]name: [#Name '==']right: [#Name 'n']]then: [#Block [#SelfAssignment left: [#Name 'count']name: [# '+=']right: [#Int '1']]]]]]]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'count']]]]]except: [# [#Except cond: [#Name 'EOFError']body: [#Block [#Break 'break']]]]]
# 入力された文字列の整数値をnとする
n = int(input())
# {{'0からn未満までの数列}}の各要素を_とし、入力された文字列の整数値の列をaとする
a = [int(input()) for _ in range(n)]
# -10000000000をmaxvとする
maxv = -10000000000
# aの最初値をminvとする
minv = a[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1,n) :
  # maxvとa(i)からminvを引いた値の最大値をmaxvとする
  maxv = max(maxv,a[i] - minv)
  # minvとa(i)の最小値をminvとする
  minv = min(minv,a[i])
# maxvを出力する
print(maxv)
Syntax Error ((unknown source):8:14+186)
        elif i == '-':
              ^       
# 空列をxとする
x = []
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをSとする
S = list(map(int,input().split()))
# 入力された文字列の整数値をqとする
q = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをTとする
T = list(map(int,input().split()))
# 関数Searchを[#FuncParam [#ParamDecl name: [#Name 'data']][#ParamDecl name: [#Name 'value']]]のパラメータを持つように定義する
def Search (data, value) :
  # '0からdataの長さ未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(len(data)) :
    # data(i)がvalueのとき、
    if data[i] == value :
      # iを関数出力とする
      return i
  # -1を関数出力とする
  return -1
# '0からq未満までの数列の各要素を順にjとして、繰り返す
for j  in range(q) :
  # Search(S,T(j))が-1より大きいとき、
  if Search(S, T[j])  > -1 :
    # x.append(Search(S, T[j]))
    x.append(Search(S, T[j]))
# xの長さを出力する
print(len(x))
# 関数Search2を[#FuncParam [#ParamDecl name: [#Name 'data']][#ParamDecl name: [#Name 'value']]]のパラメータを持つように定義する
def Search2 (data, value) :
  # 0をleftとする
  left = 0
  # dataの長さから1を引いた値をrightとする
  right = len(data) - 1
  # leftがright以下の間、繰り返す
  while left <= right :
    # ({{leftにrightを加えた値}})の組を2で割った商をmidとする
    mid = (left + right) // 2
    # data(mid)がvalueのとき、
    if data[mid] == value :
      # midを関数出力とする
      return mid
    # ('data(mid)がvalueより小さい',)
    elif data[mid] < value :
      # midに1を加えた値をleftとする
      left = mid + 1
    # ()
    else :[#Else [#Block [#VarDecl name: [#Name 'right']expr: [#Infix left: [#Name 'mid']name: [#Name '-']right: [#Int '1']]]]]
  # -1を関数出力とする
  return -1
# 空列をxとする
x = []
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをSとする
S = list(map(int,input().split()))
# 入力された文字列の整数値をqとする
q = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをTとする
T = list(map(int,input().split()))
# '0からq未満までの数列の各要素を順にjとして、繰り返す
for j  in range(q) :
  # Search2(S,T(j))が-1より大きいとき、
  if Search2(S, T[j])  > -1 :
    # x.append(Search2(S, T[j]))
    x.append(Search2(S, T[j]))
# xの長さを出力する
print(len(x))
Syntax Error ((unknown source):2:10+27)
@functools.lru_cache(maxsize=30)
          ^                     