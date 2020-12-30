# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def gcd (x,y) :
  # xがyより小さいとき、
  if x < y :
    # xとyを入れ替える
    x, y = y, x
  # yが0のとき、
  if y == 0 :
    # xを関数出力とする
    return x
  # gcd(y,xをyで割った余り)を関数出力とする
  return gcd(y, x % y)
# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x,y  = map(int,input().split())
# 0をansとする
ans = 0
# gcd(x,y)をansとする
ans = gcd(x,y)
# ansを出力する
print(ans)