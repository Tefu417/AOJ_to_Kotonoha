# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def gcd (a,b) :
  # bの間、繰り返す
  while b :
    # bとaをbで割った余りをaとbとする
    a,b = b,a%b
  # aを関数出力とする
  return a
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def lcm (a,b) :
  # aをgcd(a,b)で割った商にbを掛けた値を関数出力とする
  return a//gcd(a,b)*b
# 入力された文字列
input()
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