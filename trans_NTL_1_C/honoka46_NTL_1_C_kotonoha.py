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
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def lcm (a,b) :
  # aをgcd(a,b)で割った商にbを掛けた値を関数出力とする
  return a//gcd(a,b)*b
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# 1をbとする
b = 1
# aの各要素を順にiとして、繰り返す
for i  in a :
  # lcm(b,i)をbとする
  b = lcm(b,i)
# bを出力する
print(b)