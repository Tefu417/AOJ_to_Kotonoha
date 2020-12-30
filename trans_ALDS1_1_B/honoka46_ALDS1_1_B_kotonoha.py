# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def gcd (a,b) :
  # aがbより小さいとき、
  if a<b :
    # aとbを入れ替える
    a, b = b, a
  # bが0のとき、
  if b==0 :
    # aを関数出力とする
    return a
  # gcd(b,aをbで割った余り)を関数出力とする
  return gcd(b,a%b)
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a,b = map(int,input().split())
# 0をgとする
g = 0
# gcd(a,b)をgとする
g = gcd(a,b)
# gを出力する
print(g)