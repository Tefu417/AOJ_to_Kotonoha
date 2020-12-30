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