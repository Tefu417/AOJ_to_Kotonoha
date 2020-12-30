
# 識別子が'__main__'のとき、
if __name__ == '__main__' :
  # 'Hello World'を出力する
  print('Hello World')
# 入力された文字列の整数値の3乗を出力する
print(int(input())**3)
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# aにbを掛けた値と((end, ' '))からなる辞書を出力する
print(a * b, end=' ')
# 2に({{aにbを加えた値}})の組を掛けた値を出力する
print(2 * (a + b))
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# aがbより大きいとき'>'、そうでなければ{{aがbより小さい}}とき'<'、そうでなければ'=='をoperatorとする
operator = '>' if a > b else '<' if a < b else '=='
# format(operator)を出力する
print("a {} b".format(operator))
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a, b, c  = map(int, input().split())
# {{aがbより小さいかどうか}}がcより小さいとき'Yes'、そうでなければ'No'をanswerとする
answer = 'Yes' if a < b < c else 'No'
# answerを出力する
print(answer)
# sysモジュールを用いる
import sys
# sys.stdinをfとする
f = sys.stdin
# 関数mainを[#FuncParam [#ParamDecl name: [#Name 'f']]]のパラメータを持つように定義する
def main (f) :
  # map(整数,f.readline()を空白で分割した列)を展開し順にnormal、express、bothとする
  normal, express, both  = map(int, f.readline().split())
  # (normal、かつexpress)の組、またはbothのとき'Open'、そうでなければ'Close'を出力する
  print('Open' if (normal and express) or both else 'Close')
# main(f)
main(f)
# 入力された文字列の整数値をSとする
S = int(input())
# Sを3600で割った値の整数値をhとする
h = int(S / 3600)
# ({{Sを3600で割った余り}})の組を60で割った値の整数値をmとする
m = int((S % 3600) / 60)
# Sを60で割った余りをsとする
s = S % 60
# h、m、s、((sep, ':'))からなる辞書を出力する
print(h,m,s,sep=':')
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# aをbで割った値の整数値をdとする
d = int(a / b)
# aをbで割った余りをrとする
r = a % b
# aをbで割った値をfとする
f = a / b
# d、r、format(f)を出力する
print(d, r,"{:f}".format(f))
# mathモジュールを用いる
import math
# 入力された文字列の浮動小数点数値をrとする
r = float(input())
# math.piに(rの2乗)の組を掛けた値をareaとする
area = math.pi * (r ** 2)
# 2にmath.piを掛けた値にrを掛けた値をcircumferenceとする
circumference = 2 * math.pi * r
# テンプレートareaをcircumferenceでフォーマットした文字列を出力する
print("{:f} {:f}".format(area, circumference))
# sysモジュールを用いる
import sys
# sys.stdinをfとする
f = sys.stdin
# map(整数,f.readline()を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, f.readline().split())
# format({{{{aにbを掛けた値}}を3.305785で割った値}})を出力する
print('{:.6f}'.format(a * b / 3.305785))
# *({{map(整数,{{input()を空白で分割した列}})をソートした列}})を出力する
print(*sorted(map(int, input().split())))
# map(整数,入力された文字列を空白で分割した列)を展開し順にW、H、x、y、rとする
W, H, x, y, r  = map(int, input().split())
# {{{{rがx以下かどうか}}が{{Wからrを引いた値}}以下}}、かつ{{{{rがy以下かどうか}}が{{Hからrを引いた値}}以下かどうか}}のとき'Yes'、そうでなければ'No'を出力する
print( 'Yes' if r <= x <= W - r and r <= y <= H - r else 'No')
# sysモジュールを用いる
import sys
# sys.stdinをfとする
f = sys.stdin
# (未定値、6000、4000、3000、2000)からなる列をvaluesとする
values = [None,6000,4000,3000,2000]
# fの各要素を順にlineとして、繰り返す
for line  in f :
  # map(整数,lineを空白で分割した列)を展開し順にtとnとする
  t, n  = map(int, line.split())
  # values(t)にnを掛けた値を出力する
  print(values[t] * n)
# sysモジュールを用いる
import sys
# sys.stdinをfとする
f = sys.stdin
# fの各要素を順にlineとして、繰り返す
for line  in f :
  # map(整数,lineを空白で分割した列)を展開し順にaとbとする
  a, b  = map(int, line.split())
  # aからbを引いた値を出力する
  print(a - b)
# sysモジュールを用いる
import sys
# {{sys.stdinの各要素をiとし、iの整数値の列}}の総和を出力する
print(sum(int(i) for i in sys.stdin))
Syntax Error ((unknown source):1:11+11)
import sys, itertools
           ^         
# mathモジュールを用いる
import math
# 関数roundup1000を[#FuncParam [#ParamDecl name: [#Name 'num']]]のパラメータを持つように定義する
def roundup1000 (num) :
  # math.ceil(num  / 1000) に1000を掛けた値を関数出力とする
  return math.ceil(num  / 1000) * 1000
# 100000をdebtとする
debt = 100000
# '0から入力された文字列の整数値未満までの数列の各要素を順に_として、繰り返す
for _  in range(int(input())) :
  # roundup1000(debtに1.05を掛けた値)をdebtとする
  debt = roundup1000(debt * 1.05)
# debtを出力する
print(debt)
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a, b, c  = map(int, input().split())
# 0をcountとする
count = 0
# 'aからbに1を加えた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(a, b + 1) :
  # cをiで割った余りが0のとき、
  if c % i == 0 :
    # ([[#Name 'count'], [#Int '1']],)
    [[#Name 'count'], [#Int '1']]
# countを出力する
print(count)
# '1から10未満までの数列の各要素を順にpreとして、繰り返す
for pre  in range(1, 10) :
  # '1から10未満までの数列の各要素を順にpostとして、繰り返す
  for post  in range(1, 10) :
    # format(pre,post,{{preにpostを掛けた値}})を出力する
    print('{}x{}={}'.format(pre, post, pre * post))
# '#.'に151を掛けた値をtmpとする
tmp = '#.' * 151
# 関数drawを[#FuncParam [#ParamDecl name: [#Name 'H']][#ParamDecl name: [#Name 'W']]]のパラメータを持つように定義する
def draw (H, W) :
  # tmpの位置先頭から位置Wまでの部分をoddとする
  odd = tmp[:W]
  # tmpの位置1から位置Wに1を加えた値までの部分をevenとする
  even = tmp[1:W + 1]
  # {{({{odd + '\n' + even に'\n'を加えた値}})の組に({{Hを2で割った商}})の組を掛けた値}}に({{{{Hを2で割った余りの}}とき{{oddに'\n'を加えた値}}、そうでなければ''}})の組を加えた値を出力する
  print((odd + '\n' + even + '\n') * (H // 2) + (odd  + '\n' if H % 2 else ''))
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にHとWとする
  H, W  = map(int, input().split())
  # HがWかどうかが0のとき、
  if H == W == 0 :
    # 繰り返すのを中断する
    break
  # draw(H,W)
  draw(H, W)
Syntax Error ((unknown source):1:11+11)
import sys, operator
           ^        
# 入力された文字列をnとする
n = input()
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int, input().split()))
# aの最小値、aの最大値、aの総和を出力する
print(min(a), max(a), sum(a))
# 関数memoizeを[#FuncParam [#ParamDecl name: [#Name 'f']]]のパラメータを持つように定義する
def memoize (f) :
  # 空辞書をcacheとする
  cache = {}  
  # 関数helperを[#FuncParam [#ParamDecl name: [#Name 'x']]]のパラメータを持つように定義する
  def helper (x) :
    # not in(x,cache)のとき、
    if x not in cache :
      # f(x)をcache[x] にする
      cache[x]  = f(x)  
    # cache(x)を関数出力とする
    return cache[x]  
  # helperを関数出力とする
  return helper
# 関数fibを[#FuncParam [#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def fib (n) :
  # nが(0と1)の組に含まれるとき、
  if n in (0, 1) :
    # 1を関数出力とする
    return 1
  # ()
  else :[#Else [#Block [#Return expr: [#Infix left: [#ApplyExpr name: [#Name 'fib']params: [#Arguments [#Infix left: [#Name 'n']name: [#Name '-']right: [#Int '1']]]]name: [#Name '+']right: [#ApplyExpr name: [#Name 'fib']params: [#Arguments [#Infix left: [#Name 'n']name: [#Name '-']right: [#Int '2']]]]]]]]
# fib(入力された文字列の整数値)を出力する
print(fib(int(input())))
Syntax Error ((unknown source):3:-1+52)
    turn60 = 0.5 + 3 ** 0.5 * 0.5j
                                  
# 入力された文字列をnとする
n = input()
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int, input().split()))
# a.reverse()
a.reverse()
# *(a)を出力する
print(*a)
# {{'0から10未満までの数列}}の各要素を_とし、入力された文字列の整数値の列をmountainsとする
mountains = [int(input()) for _ in range(10)]
# {{mountainsをソートした列}}の先頭-3個を取り除いた部分の逆順の各要素を順にheightとして、繰り返す
for height  in sorted(mountains)[-3:][::-1] :
  # heightを出力する
  print(height)
# 入力された文字列を英大文字に変換した文字列を出力する
print(input().upper())
# 入力された文字列の英大文字を英小文字、英小文字を英大文字に変換した文字列を出力する
print(input().swapcase())
Syntax Error ((unknown source):1:11+11)
import sys, string
           ^      
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列)の総和をxとする
  x = sum(map(int,input()))
  # xのとき、
  if x :
    # xを出力する
    print(x)
  # ()
  else :[#Else [#Block [#Break 'break']]]
# sysモジュールを用いる
import sys
# 入力された文字列を英小文字に変換した文字列をkeywordとする
keyword = input().lower()
# 0をcountとする
count = 0
# sys.stdinの各要素を順にlineとして、繰り返す
for line  in sys.stdin :
  # ([[#Name 'count'], [#ApplyExpr name: [#Name 'sum']params: [#Arguments [#List [#ForExpr append: [#Int '1']each: [# [#Name 'word']]list: [#MethodExpr recv: [#MethodExpr recv: [#Name 'line']name: [#Name 'lower']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]cond: [#Infix left: [#Name 'word']name: [#Name '==']right: [#Name 'keyword']]]]]]],)
  [[#Name 'count'], [#ApplyExpr name: [#Name 'sum']params: [#Arguments [#List [#ForExpr append: [#Int '1']each: [# [#Name 'word']]list: [#MethodExpr recv: [#MethodExpr recv: [#Name 'line']name: [#Name 'lower']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]cond: [#Infix left: [#Name 'word']name: [#Name '==']right: [#Name 'keyword']]]]]]]
# countを出力する
print(count)
# 入力された文字列をsとする
s = input()
# 入力された文字列をpとする
p = input()
# {{({{sに2を掛けた値}})の組内のpの出現をカウントした整数の}}とき'Yes'、そうでなければ'No'を出力する
print('Yes' if (s * 2).count(p) else 'No')
# 0と0をt_pointとh_pointとする
t_point, h_point  = 0, 0
# 入力された文字列の整数値をnとする
n = int(input())
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # 入力された文字列を空白で分割した列を展開し順にt_cardとh_cardとする
  t_card, h_card  = input().split()
  # t_cardがh_cardのとき、
  if t_card == h_card :
    # ([[#Name 't_point'], [#Int '1']],)
    [[#Name 't_point'], [#Int '1']]
    # ([[#Name 'h_point'], [#Int '1']],)
    [[#Name 'h_point'], [#Int '1']]
  # ('t_cardがh_cardより大きい',)
  elif t_card > h_card :
    # ([[#Name 't_point'], [#Int '3']],)
    [[#Name 't_point'], [#Int '3']]
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 'h_point']name: [# '+=']right: [#Int '3']]]]
# t_pointとh_pointを出力する
print(t_point, h_point)
# map(float,入力された文字列を空白で分割した列)を展開し順にx1、y1、x2、y2とする
x1, y1, x2, y2  = map(float, input().split())
# ({{(x1 - x2) の2乗に(y1 - y2) の2乗を加えた値}})の組の0.5乗を出力する
print(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
# mathモジュールを用いる
import math
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、Cとする
a, b, C  = map(int, input().split())
# bにmath.sin(math.radians(C))を掛けた値をhとする
h = b * math.sin(math.radians(C))
# aにhを掛けた値に0.5を掛けた値をSとする
S = a * h * 0.5
# aにbを加えた値にmath.sqrt(pow(a, 2) + pow(b, 2) - 2 * a * b *math.cos(math.radians(C)))を加えた値をLとする
L = a + b + math.sqrt(pow(a, 2) + pow(b, 2) - 2 * a * b *math.cos(math.radians(C)))
# Sを出力する
print(S)
# Lを出力する
print(L)
# hを出力する
print(h)
# mathモジュールを用いる
import math
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをsとする
  s = list(map(int, input().split()))
  # sの総和をnで割った値をaveとする
  ave = sum(s) / n
  # math.sqrt(sum((ave - si) ** 2 for si in s) / n)をdevとする
  dev = math.sqrt(sum((ave - si) ** 2 for si in s) / n)
  # format(dev)を出力する
  print("{:.8f}".format(dev))    
# sysモジュールを用いる
import sys
# sys.stdinの各要素を順にlineとして、繰り返す
for line  in sys.stdin :
  # map(整数,lineを空白で分割した列)を展開し順にm、f、rとする
  m, f, r  = map(int, line.split())
  # {{mがfかどうか}}がrかどうかが-1のとき、
  if m == f == r == -1 :
    # 繰り返すのを中断する
    break
  # mが-1、またはfが-1のとき、
  if m == -1 or f == -1 :
    # 'F'を出力する
    print('F')
  # ('({{mにfを加えた値}})の組が80以上の',)
  elif (m + f) >= 80 :
    # 'A'を出力する
    print('A')
  # ('({{mにfを加えた値}})の組が65以上の',)
  elif (m + f) >= 65 :
    # 'B'を出力する
    print('B')
  # ('({{mにfを加えた値}})の組が50以上の',)
  elif (m + f) >= 50 :
    # 'C'を出力する
    print('C')
  # ('({{mにfを加えた値}})の組が30以上の',)
  elif (m + f) >= 30 :
    # rが50以上のとき、
    if r >= 50 :
      # 'C'を出力する
      print('C')
    # ()
    else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString "'D'"]]]]]]
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString "'F'"]]]]]]
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にnとxとする
  n, x  = map(int, input().split())
  # nがxかどうかが0のとき、
  if n == x == 0 :
    # 繰り返すのを中断する
    break
  # 0をresultとする
  result = 0
  # '1からxを3で割った商未満までの数列の各要素を順にaとして、繰り返す
  for a  in range(1, x // 3) :
    # 'aに1を加えた値からxを2で割った商未満までの数列の各要素を順にbとして、繰り返す
    for b  in range(a + 1,  x // 2) :
      # xからaを引いた値からbを引いた値をcとする
      c = x - a - b
      # bがcより小さいかどうかがn以下のとき、
      if b < c <= n :
        # ([[#Name 'result'], [#Int '1']],)
        [[#Name 'result'], [#Int '1']]
  # resultを出力する
  print(result)
# map(整数,入力された文字列を空白で分割した列)を展開し順にn、m、Lとする
n, m, L  = map(int, input().split())
# {{'0からn未満までの数列}}の各要素を_とし、'map(整数,{{input()を空白で分割した列}})のリストの列をaとする
a = [list(map(int, input().split())) for _ in range(n)]
# {{'0からm未満までの数列}}の各要素を_とし、'map(整数,{{input()を空白で分割した列}})のリストの列をbとする
b = [list(map(int, input().split())) for _ in range(m)]
# aの各要素をaiとし、{{{{*bの要素をそれぞれ組にした列}}の各要素をbjとし、ak * bk for ak, bk in zip(ai,bj)の総和の列}}の列をcとする
c = [[sum(ak * bk for ak, bk in zip(ai,bj)) for bj in zip(*b)] for ai in a]
# cの各要素を順にciとして、繰り返す
for ci  in c :
  # *(ci)を出力する
  print(*ci)
# 関数powerを[#FuncParam [#ParamDecl name: [#Name 'm']][#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def power (m, n) :
  # nのとき、
  if n :
    # power({{{{mにmを掛けた値}}を1000000007で割った余り}},{{nを2で割った商}})に({{{{nを2で割った余りの}}ときm、そうでなければ1}})の組を掛けた値を1000000007で割った余りを関数出力とする
    return power(m * m % 1000000007, n // 2) * (m if n % 2 else 1) % 1000000007
  # 1を関数出力とする
  return 1[#FromDecl name: [#ModuleName 'sys']names: [# [#Name 'stdin']]]
# stdin.readlineをreadlineとする
readline = stdin.readline
# map(整数,readline()を空白で分割した列)を展開し順にmとnとする
m, n  = map(int, readline().split())
# power(m,n)を出力する
print(power(m, n))
# 関数euclidean_algorithmを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def euclidean_algorithm (x, y) :
  # 0をcntとする
  cnt = 0
  # xがyより小さいとき、
  if x < y :
    # xとyを入れ替える
    x, y = y, x
  # yの間、繰り返す
  while y :
    # xをyで割った余りをxとする
    x = x % y
    # xとyを入れ替える
    x, y = y, x
    # ([[#Name 'cnt'], [#Int '1']],)
    [[#Name 'cnt'], [#Int '1']]
  # (xとcnt)の組を関数出力とする
  return x, cnt
# sysモジュールを用いる
import sys
# sys.stdinをfとする
f = sys.stdin
# 真の間、繰り返す
while True :
  # map(整数,f.readline()を空白で分割した列)を展開し順にaとbとする
  a, b  = map(int, f.readline().split())
  # aが0のとき、
  if a == 0 :
    # 繰り返すのを中断する
    break
  # *(euclidean_algorithm(a,b))を出力する
  print(*euclidean_algorithm(a, b))
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# aがbより小さいとき(aとb)の組、そうでなければ(bとa)の組を展開し順にminiとbigとする
mini, big  = (a, b) if a < b else (b, a)
# 真の間、繰り返す
while True :
  # bigをminiで割った余りをremとする
  rem = big % mini
  # remが0のとき、
  if rem == 0 :
    # 繰り返すのを中断する
    break
  # remとminiをminiとbigとする
  mini, big  = rem, mini
# miniを出力する
print(mini)
# sysモジュールを用いる
import sys
# sys.stdinの各要素を順にlineとして、繰り返す
for line  in sys.stdin :
  # lineの整数値をdとする
  d = int(line)
  # {{{{'dから600未満までのd間隔の数列}}の各要素をiとし、{{{{iにiを掛けた値}}にdを掛けた値}}の列}}の総和を出力する
  print(sum(i * i * d for i in range(d, 600, d)))
# sysモジュールを用いる
import sys
# sys.stdinの各要素を順にlineとして、繰り返す
for line  in sys.stdin :
  # map(整数,lineを空白で分割した列)を展開し順にa、b、c、d、e、fとする
  a, b, c, d, e, f  = map(int, line.split())
  # ({{{{aにfを掛けた値}}から{{dにcを掛けた値}}を引いた値}})の組を({{{{aにeを掛けた値}}から{{bにdを掛けた値}}を引いた値}})の組で割った値をyとする
  y = (a * f - d * c) / (a * e - b * d)
  # ({{{{cにeを掛けた値}}から{{bにfを掛けた値}}を引いた値}})の組を({{{{aにeを掛けた値}}から{{bにdを掛けた値}}を引いた値}})の組で割った値をxとする
  x = (c * e - b * f) / (a * e - b * d)
  # xが0のとき、
  if x == 0 :
    # xの絶対値をxとする
    x = abs(x)
  # yが0のとき、
  if y == 0 :
    # yの絶対値をxとする
    x = abs(y)       
  # テンプレートxをyでフォーマットした文字列を出力する
  print('{:.3f} {:.3f}'.format(x, y))
# sysモジュールを用いる
import sys
# sys.stdinをfとする
f = sys.stdin
# 真の間、繰り返す
while True :
  # f.readline()の整数値をqとする
  q = int(f.readline())
  # qが-1のとき、
  if q == -1 :
    # 繰り返すのを中断する
    break
  # qを2で割った値をxとする
  x = q / 2
  # {{xの3乗からqを引いた値}}の絶対値が0.00001にqを掛けた値以上の間、繰り返す
  while abs(x ** 3 - q) >= 0.00001 * q :
    # xから({{xの3乗からqを引いた値}})の組を({{3にxの2乗を掛けた値}})の組で割った値を引いた値をxとする
    x = x - (x ** 3 - q) / (3 * x ** 2)
  # format(x)を出力する
  print('{:.6f}'.format(x))
Syntax Error ((unknown source):6:35+72)
print(*[word for word in re.split(r'\s|,|\.', f.readline()) if 3 <= len(word) <= 6])
                                   ^                                                
# 入力された文字列の逆順を出力する
print(input()[::-1])
# sysモジュールを用いる
import sys
# sys.stdinをfとする
f = sys.stdin
# 関数is_symmetryを[#FuncParam [#ParamDecl name: [#Name 's']]]のパラメータを持つように定義する
def is_symmetry (s) :
  # sがsの逆順かどうかを関数出力とする
  return s == s[::-1]
# {{fの各要素をlineとし、is_symmetry({{lineの両端から空白改行を取り除いた文字列}})のときの1の列}}の総和を出力する
print(sum(1 for line in f if is_symmetry(line.strip())))
# collectionsモジュールを用いる
import collections
# collections.Counter(input().split())をcとする
c = collections.Counter(input().split())
# ''をlongestとする
longest = ''
# cの各要素を順にwordとして、繰り返す
for word  in c :
  # longestの長さがwordの長さより小さいとき、
  if len(longest) < len(word) :
    # wordをlongestとする
    longest = word
# c.most_common(1)の最初値の最初値とlongestを出力する
print(c.most_common(1)[0][0], longest)
# sysモジュールを用いる
import sys
# sys.stdinをfとする
f = sys.stdin
# f.readline()を空白で分割した列をsentencesとする
sentences = f.readline().split()
# '0からsentencesの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(sentences)) :
  # 'apple'がsentences(i)に含まれるとき、
  if 'apple' in sentences[i] :
    # sentences(i)内の'apple'を'peach'で置き換えた文字列をsentences[i] にする
    sentences[i]  = sentences[i].replace('apple', 'peach')
  # ("'peach'がsentences(i)に含まれる",)
  elif 'peach' in sentences[i] :
    # sentences(i)内の'peach'を'apple'で置き換えた文字列をsentences[i] にする
    sentences[i]  = sentences[i].replace('peach', 'apple')
# sentencesを文字列' 'で連結した文字列を出力する
print(' '.join(sentences))
# sysモジュールを用いる
import sys
# sys.stdinをfとする
f = sys.stdin
# stringモジュールを用いる
import string
# 0をsecretとする
secret = 0
# fの各要素を順にlineとして、繰り返す
for line  in f :
  # 'lineのリストをlineとする
  line = list(line)
  # '0からlineの長さ未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(len(line)) :
    # not in(line(i),string.digits)のとき、
    if line[i] not in string.digits :
      # ' 'をline[i] にする
      line[i]  = ' '
  # ([[#Name 'secret'], [#ApplyExpr name: [#Name 'sum']params: [#Arguments [#ApplyExpr name: [#Name 'map']params: [#Arguments [#Name 'int'][#MethodExpr recv: [#MethodExpr recv: [#QString "''"]name: [#Name 'join']params: [#Arguments [#Name 'line']]]name: [#Name 'split']params: [#Arguments '']]]]]]],)
  [[#Name 'secret'], [#ApplyExpr name: [#Name 'sum']params: [#Arguments [#ApplyExpr name: [#Name 'map']params: [#Arguments [#Name 'int'][#MethodExpr recv: [#MethodExpr recv: [#QString "''"]name: [#Name 'join']params: [#Arguments [#Name 'line']]]name: [#Name 'split']params: [#Arguments '']]]]]]]
# secretを出力する
print(secret)
# sysモジュールを用いる
import sys
# sys.stdinの各要素をlineとし、'map(整数,{{lineを空白で分割した列}})のリストの列をlinesとする
lines = [list(map(int, line.split())) for line in sys.stdin]
# '0からlinesの長さ未満までの2間隔の数列の各要素を順にiとして、繰り返す
for i  in range(0, len(lines), 2) :
  # lines(i)をaとする
  a = lines[i]
  # lines(iに1を加えた値)をbとする
  b = lines[i + 1]
  # {{'0からaの長さ未満までの数列}}の各要素をiとし、{{a(i)がb(i)の}}ときの1の列の総和をhitとする
  hit = sum(1 for i in range(len(a)) if a[i] == b[i])
  # {{bの各要素をbiとし、{{biがaに含まれる}}ときの1の列}}の総和からhitを引いた値をblowとする
  blow = sum(1 for bi in b if bi in a) - hit
  # hitとblowを出力する
  print(hit, blow)  
[#FromDecl name: [#ModuleName 'sys']names: [# [#Name 'stdin']]]
# stdin.readlineをreadlineとする
readline = stdin.readline
# 真の間、繰り返す
while True :
  # readline()の整数値をold_room_numとする
  old_room_num = int(readline())
  # old_room_numが0のとき、
  if old_room_num == 0 :
    # 繰り返すのを中断する
    break
  # old_room_numの8進文字列の先頭2個を取り除いた部分をoctalとする
  octal = oct(old_room_num)[2:]
  # octal.translate(str.maketrans('4567', '5789'))をnew_room_numとする
  new_room_num = octal.translate(str.maketrans('4567', '5789'))
  # new_room_numを出力する
  print(new_room_num)
# sysモジュールを用いる
import sys
# sys.stdinをfとする
f = sys.stdin
# stringモジュールを用いる
import string
# 'a'の順序数をOFFSETとする
OFFSET = ord('a')
# 関数to_gammaを[#FuncParam [#ParamDecl name: [#Name 'c']]]のパラメータを持つように定義する
def to_gamma (c) :
  # cの順序数からOFFSETを引いた値を関数出力とする
  return ord(c) - OFFSET
# 関数from_gammaを[#FuncParam [#ParamDecl name: [#Name 'gamma']][#ParamDecl name: [#Name 'alpha']][#ParamDecl name: [#Name 'beta']]]のパラメータを持つように定義する
def from_gamma (gamma, alpha, beta) :
  # 文字コード{{({{alpha * gamma にbetaを加えた値}})の組を26で割った余り}}にOFFSETを加えた値の文字を関数出力とする
  return chr((alpha * gamma + beta) % 26 + OFFSET) 
# 関数affineを[#FuncParam [#ParamDecl name: [#Name 'c']][#ParamDecl name: [#Name 'alpha']][#ParamDecl name: [#Name 'beta']]]のパラメータを持つように定義する
def affine (c, alpha, beta) :
  # from_gamma(to_gamma(c),alpha,beta)を関数出力とする
  return from_gamma(to_gamma(c), alpha, beta)[#Document [# 'g[0]==g[3]である前提']]
# 関数search_thatを[#FuncParam [#ParamDecl name: [#Name 'w']]]のパラメータを持つように定義する
def search_that (w) :
  # to_gamma(w(2))をbとする
  b = to_gamma(w[2])
  # '0から26未満までの数列の各要素を順にaとして、繰り返す
  for a  in range(26) :
    # w(0)がaffine('t',a,b)、かつw(1)がaffine('h',a,b)のとき、
    if w[0] == affine('t',a,b) and w[1] == affine('h',a,b) :
      # (aとb)の組を関数出力とする
      return a, b
  # (-1と-1)の組を関数出力とする
  return -1, -1
# 関数search_thisを[#FuncParam [#ParamDecl name: [#Name 'w']]]のパラメータを持つように定義する
def search_this (w) :
  # ({{{{to_gamma(w[0])からto_gamma(w[3])を引いた値}}に26を加えた値}})の組を26で割った余りをaとする
  a = (to_gamma(w[0]) - to_gamma(w[3]) + 26) % 26
  # '0から26未満までの数列の各要素を順にbとして、繰り返す
  for b  in range(26) :
    # {{w(0)がaffine('t',a,b)}}、かつ{{w(1)がaffine('h',a,b)かどうか}}、かつ{{w(2)がaffine('i',a,b)かどうか}}、かつw(3)がaffine('s',a,b)のとき、
    if w[0] == affine('t',a,b) and w[1] == affine('h',a,b) and w[2] == affine('i',a,b) and w[3] == affine('s',a,b) :
      # (aとb)の組を関数出力とする
      return a, b
  # (-1と-1)の組を関数出力とする
  return -1, -1
# 関数searchを[#FuncParam [#ParamDecl name: [#Name 'w']]]のパラメータを持つように定義する
def search (w) :
  # w(0)がw(3)のとき、
  if w[0] == w[3] :
    # search_that(w)を関数出力とする
    return search_that(w)
  # ()
  else :[#Else [#Block [#Return expr: [#ApplyExpr name: [#Name 'search_this']params: [#Arguments [#Name 'w']]]]]]
# f.readline()の整数値をnとする
n = int(f.readline())
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # f.readline()の両端から空白改行を取り除いた文字列をlineとする
  line = f.readline().strip()
  # {{lineを空白で分割した列}}の各要素をwordとし、{{wordの長さが4の}}ときのwordの列をwordsとする
  words = [word for word in line.split() if len(word) == 4]
  # wordsの各要素を順にwordとして、繰り返す
  for word  in words :
    # search(word)を展開し順にaとbとする
    a, b  = search(word)
    # aが-1と等しくないとき、
    if a != -1 :
      # line.translate(str.maketrans(''.join([affine(c, a, b) for c in string.ascii_lowercase]), string.ascii_lowercase))を出力する
      print(line.translate(str.maketrans(''.join([affine(c, a, b) for c in string.ascii_lowercase]), string.ascii_lowercase)))
      # 繰り返すのを中断する
      break
# sysモジュールを用いる
import sys
# sys.stdinをfとする
f = sys.stdin
# fの各要素を順にlineとして、繰り返す
for line  in f :
  # lineの両端から空白改行を取り除いた文字列をlineとする
  line = line.strip()
  # lineの先頭から'@'を探して見つかった位置をindexとする
  index = line.find('@')
  # indexが-1と等しくない間、繰り返す
  while index != -1 :
    # lineの位置indexから位置indexに3を加えた値までの部分をtargetとする
    target = line[index:index + 3]
    # line内のtargetをtarget(2)にtarget(1)の整数値を掛けた値で置き換えた文字列をlineとする
    line = line.replace(target, target[2] * int(target[1]))
    # lineの先頭から'@'を探して見つかった位置をindexとする
    index = line.find('@')
  # lineを出力する
  print(line)
# 関数longest_commonを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def longest_common (x, y) :
  # (0)からなる列をcostとする
  cost = [0]
  # yの各要素を順にcとして、繰り返す
  for c  in y :
    # 'costの長さから1を引いた値から-1未満までの-1間隔の数列の各要素を順にiとして、繰り返す
    for i  in range(len(cost) -1, -1, -1) :
      # xの位置cost(i)からcを探して見つかった位置に1を加えた値をindexとする
      index = x.find(c, cost[i]) + 1
      # indexのとき、
      if index :
        # iに1を加えた値がcostの長さより小さいとき、
        if i + 1 < len(cost) :
          # cost({{iに1を加えた値}})とindexの最小値をcost[i + 1] にする
          cost[i + 1]  = min(cost[i + 1], index)
        # ()
        else :[#Else [#Block [#Expression [#MethodExpr recv: [#Name 'cost']name: [#Name 'append']params: [#Arguments [#Name 'index']]]]]]
  # costの長さから1を引いた値を関数出力とする
  return len(cost)  - 1
# 入力された文字列の整数値をnとする
n = int(input())
# '0からn未満までの数列の各要素を順に_として、繰り返す
for _  in range(n) :
  # 入力された文字列をxとする
  x = input()
  # 入力された文字列をyとする
  y = input()
  # longest_common(x,y)を出力する
  print(longest_common(x, y))
Syntax Error ((unknown source):11:23+235)
        elif min(ball, *cy) == ball:
                       ^            
# 入力された文字列の整数値をNとする
N = int(input())
# {{'0からN未満までの数列}}の各要素を_とし、入力された文字列の整数値の列をRとする
R = [int(input()) for _ in range(N)]
# Rの最初値をp_buyとする
p_buy = R[0]
# R(1)をp_saleとする
p_sale = R[1]
# R(1)をbuyとする
buy = R[1]
# 未定値をsaleとする
sale = None
# '2からN未満までの数列の各要素を順にiとして、繰り返す
for i  in range(2, N) :
  # p_saleがR(i)より小さいとき、
  if p_sale < R[i] :
    # R(i)をp_saleとする
    p_sale = R[i]
  # buyがR(i)より大きいとき、
  if buy > R[i] :
    # is(sale,未定値)のとき、
    if sale is None :
      # R(i)をsaleとする
      sale = R[i]
    # p_saleからp_buyを引いた値がsaleからbuyを引いた値より小さいとき、
    if p_sale - p_buy < sale - buy :
      # saleとbuyをp_saleとp_buyとする
      p_sale, p_buy  = sale, buy 
    # 未定値とR(i)をsaleとbuyとする
    sale, buy  = None, R[i]
  # ()
  else :[#Else [#Block [#If cond: [#Or left: [#Infix left: [#Name 'sale']name: [#Name 'is']right: [#Null 'None']]right: [#Infix left: [#Name 'sale']name: [#Name '<']right: [#IndexExpr recv: [#Name 'R']index: [#Name 'i']]]]then: [#Block [#VarDecl name: [#Name 'sale']expr: [#IndexExpr recv: [#Name 'R']index: [#Name 'i']]]]]]]
# p_saleからp_buyを引いた値をp_gainとする
p_gain = p_sale - p_buy
# is(sale,未定値)のときp_gain、そうでなければp_gainと{{saleからbuyを引いた値}}の最大値を出力する
print(p_gain if sale is None else max(p_gain, sale - buy))
# operatorモジュールを用いる
import operator
# (('+', operatorのadd)、('-', operator.sub)、('*', operator.mul))からなる辞書をfuncとする
func = {'+':operator.add, '-':operator.sub, '*':operator.mul}
# 空列をstackとする
stack = []
# 入力された文字列を空白で分割した列の各要素を順にsymbolとして、繰り返す
for symbol  in input().split() :
  # symbolが全て数字のとき、
  if symbol.isdigit() :
    # stack.append(int(symbol))
    stack.append(int(symbol))
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'a']expr: [#MethodExpr recv: [#Name 'stack']name: [#Name 'pop']params: [#Arguments '']]][#VarDecl name: [#Name 'b']expr: [#MethodExpr recv: [#Name 'stack']name: [#Name 'pop']params: [#Arguments '']]][#Expression [#MethodExpr recv: [#Name 'stack']name: [#Name 'append']params: [#Arguments [#ApplyExpr name: [#IndexExpr recv: [#Name 'func']index: [#Name 'symbol']]params: [#Arguments [#Name 'b'][#Name 'a']]]]]]]]
# stackの最初値を出力する
print(stack[0])
# sysモジュールを用いる
import sys
# map(整数,sys.stdin.readline()を空白で分割した列)を展開し順にnとqとする
n, q  = map(int, sys.stdin.readline().split())
# 空列をprocessesとする
processes = []
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # sys.stdin.readline()を空白で分割した列を展開し順にnameとtimeとする
  name, time  = sys.stdin.readline().split()
  # ([[#Name 'processes'], [#List [#List [#Name 'name'][#ApplyExpr name: [#Name 'int']params: [#Arguments [#Name 'time']]]]]],)
  [[#Name 'processes'], [#List [#List [#Name 'name'][#ApplyExpr name: [#Name 'int']params: [#Arguments [#Name 'time']]]]]]
# 0をprogressとする
progress = 0
# processesの長さの間、繰り返す
while len(processes) :
  # 空列をnew_processesとする
  new_processes = []
  # processesの各要素を順にtargetとして、繰り返す
  for target  in processes :
    # target(1)がqより大きいとき、
    if target[1] > q :
      # ([[#IndexExpr recv: [#Name 'target']index: [#Int '1']], [#Name 'q']],)
      [[#IndexExpr recv: [#Name 'target']index: [#Int '1']], [#Name 'q']]
      # ([[#Name 'progress'], [#Name 'q']],)
      [[#Name 'progress'], [#Name 'q']]
      # ([[#Name 'new_processes'], [#List [#Name 'target']]],)
      [[#Name 'new_processes'], [#List [#Name 'target']]]
    # ()
    else :[#Else [#Block [#SelfAssignment left: [#Name 'progress']name: [# '+=']right: [#IndexExpr recv: [#Name 'target']index: [#Int '1']]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#Name 'target']index: [#Int '0']][#Name 'progress']]]]]]
  # new_processesをprocessesとする
  processes = new_processes
# 入力された文字列をnとする
n = input()
# {{入力された文字列を空白で分割した列}}の各要素をiとし、iの整数値の列の集合をsとする
s = set(int(i) for i in input().split())
# 入力された文字列をqとする
q = input()
# {{入力された文字列を空白で分割した列}}の各要素をiとし、iの整数値の列の集合をtとする
t = set(int(i) for i in input().split())
# &(t,s)の長さを出力する
print(len(t & s))
# 入力された文字列をnとする
n = input()
# map(整数,{{入力された文字列を空白で分割した列}})の集合をsとする
s = set(map(int, input().split()))
# 入力された文字列をqとする
q = input()
# map(整数,{{入力された文字列を空白で分割した列}})の集合をtとする
t = set(map(int, input().split()))
# &(t,s)の長さを出力する
print(len(t & s))
Syntax Error ((unknown source):1:12+12)
import math, sys
            ^   
Syntax Error ((unknown source):31:20+694)
print(len(puddles), *puddles)
                    ^        
# itertoolsモジュールを用いる
import itertools
# 入力された文字列をnとする
n = input()
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int, input().split()))
# 入力された文字列をqとする
q = input()
# 集合をasetとする
aset = set()
# '1からaの長さに1を加えた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1, len(a) + 1) :
  # ([[#Name 'aset'], [#ApplyExpr name: [#Name 'set']params: [#Arguments [#ForExpr append: [#ApplyExpr name: [#Name 'sum']params: [#Arguments [#Name 'combi']]]each: [# [#Name 'combi']]list: [#MethodExpr recv: [#Name 'itertools']name: [#Name 'combinations']params: [#Arguments [#Name 'a'][#Name 'i']]]]]]],)
  [[#Name 'aset'], [#ApplyExpr name: [#Name 'set']params: [#Arguments [#ForExpr append: [#ApplyExpr name: [#Name 'sum']params: [#Arguments [#Name 'combi']]]each: [# [#Name 'combi']]list: [#MethodExpr recv: [#Name 'itertools']name: [#Name 'combinations']params: [#Arguments [#Name 'a'][#Name 'i']]]]]]]
# map(整数,入力された文字列を空白で分割した列)の各要素を順にmとして、繰り返す
for m  in map(int, input().split()) :
  # {{mがasetに含まれる}}とき'yes'、そうでなければ'no'を出力する
  print('yes' if m in aset else 'no')
Syntax Error ((unknown source):1:11+11)
import sys, itertools
           ^         
[#FromDecl name: [#ModuleName 'sys']names: [# [#Name 'stdin']]]
# stdin.readlineをreadlineとする
readline = stdin.readline
# ((1と3)の組、(0、2、4)の組、(1と5)の組、(0、4、6)の組、(1、3、5、7)の組、(2、4、8)の組、(3と7)の組、(4、6、8)の組、(5と7)の組)の組をadjacentとする
adjacent = (
    (1, 3),        # 0
    (0, 2, 4),     # 1
    (1, 5),        # 2
    (0, 4, 6),     # 3
    (1, 3, 5, 7),  # 4
    (2, 4, 8),     # 5
    (3, 7),        # 6
    (4, 6, 8),     # 7
    (5, 7)         # 8
)
# 関数next_boardを[#FuncParam [#ParamDecl name: [#Name 'board']][#ParamDecl name: [#Name 'space']][#ParamDecl name: [#Name 'prev']]]のパラメータを持つように定義する
def next_board (board, space, prev) :
  # adjacent(space)の各要素を順にnxtとして、繰り返す
  for nxt  in adjacent[space] :
    # nxtがprevのとき、
    if nxt == prev :
      # 最初からもう一度、繰り返す
      continue
    # boardの先頭から末尾まで(のコピー)をbとする
    b = board[:]
    # b(nxt)と0をb(space)とb(nxt)とする
    b[space], b[nxt]  = b[nxt], 0[#Yield expr: [#Tuple [#Name 'b'][#Name 'nxt']]][#FromDecl name: [#ModuleName 'heapq']names: [# [#Name 'heappop'][#Name 'heappush']]]
# (1、2、3、4、5、6、7、8、0)からなる列をendとする
end = [1, 2, 3, 4, 5, 6, 7, 8, 0][#Document [# '???????????¨????????°']]
# 1をFOREとする
FORE = 1
# 0をBACKとする
BACK = 0
# 関数searchを[#FuncParam [#ParamDecl name: [#Name 'start']]]のパラメータを持つように定義する
def search (start) :
  # startがendのとき、
  if start == end :
    # 0を関数出力とする
    return 0
  # 空辞書をtableとする
  table = {}
  # (FOREと0)の組をtable[tuple(start)] にする
  table[tuple(start)]  = (FORE, 0)
  # (BACKと0)の組をtable[tuple(end)] にする
  table[tuple(end)]  = (BACK, 0)
  # ((0、start、start.index(0)、未定値、FORE)の組と(0、end、end.index(0)、未定値、BACK)の組)からなる列をheapとする
  heap = [(0, start, start.index(0), None, FORE), (0, end, end.index(0), None, BACK)]
  # heapの間、繰り返す
  while heap :
    # heappop(heap)を展開し順にi、board、space、prev、directionとする
    i, board, space, prev, direction  = heappop(heap)
    # ([[#Name 'i'], [#Int '1']],)
    [[#Name 'i'], [#Int '1']]
    # next_board(board,space,prev)の各要素を順にbとnxtとして、繰り返す
    for b, nxt  in next_board(board, space, prev) :
      # bの組をkeyとする
      key = tuple(b)
      # keyがtableに含まれるとき、
      if key in table :
        # table(key)(0)がdirectionと等しくないとき、
        if table[key][0] != direction :
          # table(key)(1)にiを加えた値を関数出力とする
          return table[key][1] + i
        # 最初からもう一度、繰り返す
        continue
      # (directionとi)の組をtable[key] にする
      table[key]  = (direction, i)
      # bがendのとき、
      if b == end :
        # iを関数出力とする
        return i
      # heappush(heap,(i、b、nxt、space、direction)の組)
      heappush(heap, (i, b, nxt, space, direction))
# 関数mainを[#FuncParam '()']のパラメータを持つように定義する
def main () :
  # ({{'0から3未満までの数列}}の各要素を_とし、map(整数,{{readline()を空白で分割した列}})の列)の組をstartとする
  start = (map(int, readline().split()) for _ in range(3))
  # {{xの各要素をyとし、startの列}}の各要素をxとし、yの列をstartとする
  start = [y for x in start for y in x]
  # search(start)を出力する
  print(search(start))
# main()
main()