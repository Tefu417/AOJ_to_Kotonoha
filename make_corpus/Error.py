'''  else周り  '''
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"a > b"']]]]]]

Syntax Error ((unknown source):16:-1+243)
else :

'''  'が前に一つだけ入る  '''
# {{'1から31未満までの数列}}の各要素をiとし、iの列をAとする
A = [i for i in range(1, 31)]

# 'Aの集合からNの集合を引いた値のリストをRとする
R = list(set(A) - set(N))

'''  format記述  '''
Syntax Error ((unknown source):7:18+88)
print(f"{d} {r} {f:.6f}")
^
Syntax Error ((unknown source):8:10+84)
print(f"{s:.6f} {l:.6f}")
^
Syntax Error ((unknown source):5:10+66)
print(f"{S:.6f}")

'''  PJタグ？が入ってくる
    if文やfor文の中の処理がコードも出ない
    elif文の出力は（）に囲われる形でいいのか  '''
# TがHより大きいとき、
if T > H  :
# ([[#Name 't'], [#Int '3']],)
[[#Name 't'], [#Int '3']]
# ('TがHより小さい',)
elif T < H  :
# ([[#Name 'h'], [#Int '3']],)
[[#Name 'h'], [#Int '3']]
# tとhを出力する
print(t, h)

# '0から10未満までの数列の各要素を順にiとして、繰り返す
for i  in range(10)  :
# ([[#Name 's'], [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]],)
[[#Name 's'], [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]]
# sを出力する
print(s)

# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 's']expr: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 's']]]]]body: [#Block [#If cond: [#Or left: [#Infix left: [#IndexExpr recv: [#Name 's']index: [#Name 'i']]name: [#Name 'in']right: [#Name 'a']]right: [#Infix left: [#MethodExpr recv: [#IndexExpr recv: [#Name 's']index: [#Name 'i']]name: [#Name 'lower']params: [#Arguments '']]name: [#Name 'in']right: [#Name 'a']]]then: [#Block [#SelfAssignment left: [#IndexExpr recv: [#Name 'A']index: [#MethodExpr recv: [#Name 'a']name: [#Name 'index']params: [#Arguments [#MethodExpr recv: [#IndexExpr recv: [#Name 's']index: [#Name 'i']]name: [#Name 'lower']params: [#Arguments '']]]]]name: [# '+=']right: [#Int '1']]]]]]]except: [# [#Except body: [#Block [#Break 'break']]]]]

# 関数Eraを[#FuncParam [#ParamDecl name: [#Name 'P']][#ParamDecl name: [#Name 'Max']]]のパラメータを持つように定義する
def Era (P, Max)  :

# 関数primeを[#FuncParam [#ParamDecl name: [#Name 'a']]]のパラメータを持つように定義する
def prime (a)  :

'''  Syntax Error
    try, except 取れない？  '''
Syntax Error ((unknown source):43:-1+757)
except :

Syntax Error ((unknown source):27:0+403)
# Listからnumに最も近い値を返す
^
Syntax Error ((unknown source):14:18+229)
elif n % 2 == 0 :
        ^
Syntax Error ((unknown source):13:18+297)
print(f"{x:.3f} {y:.3f}")
        ^
Syntax Error ((unknown source):3:10+28)
@functools.lru_cache(maxsize = 30)

'''  reverse=真 とは出ない？  '''
# Mと((reverse, 真))からなる辞書をソートした列をMsとする
Ms = sorted(M, reverse = True)

'''  i番目とは出ない？  '''
# A(i)(j)を出力する
print(A[i][j])

'''  まんま出る  '''
# Si.append(p)
Si.append(p)

# A.append([int(a) for a in input().split()])
A.append([int(a) for a in input().split()])

# kakko.pop(-1)
kakko.pop(-1)

# math.gcd(x, y)を出力する
print(math.gcd(x, y))
