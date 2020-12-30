# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def gcd (a, b) :
  # aがbより大きいとき(aとb)からなる列、そうでなければ(bとa)からなる列を展開し順にxとyとする
  x, y  = [a, b] if a > b else [b, a]
  # yの間、繰り返す
  while y :
    # yとxをyで割った余りをxとyとする
    x, y  = y, x%y
  # xを関数出力とする
  return x
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def lcm (a, b) :
  # aにbを掛けた値をgcd(a,b)で割った商を関数出力とする
  return a*b // gcd(a, b)
# 入力された文字列の整数値をnとする
n = int(input())
# {{入力された文字列を' 'で分割した列}}の各要素をxとし、xの整数値の列をAとする
A = [int(x) for x in input().split(' ')]
# Aの最初値をtmpとする
tmp = A[0]
# '1からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1, n) :
  # lcm(tmp,A(i))をtmpとする
  tmp = lcm(tmp, A[i])
# tmpを出力する
print(tmp)