# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def gcd (x,y) :
  # yが0より大きい間、繰り返す
  while y > 0 :
    # xをyで割った余りをrとする
    r = x%y
    # yをxとする
    x = y
    # rをyとする
    y = r
  # xを関数出力とする
  return x
# map(整数,入力された文字列を空白で分割した列)を展開し順にXとYとする
X,Y  = map(int,input().split())
# XとYの最大値とXとYの最小値をxとyとする
x,y = max(X,Y),min(X,Y)
# gcd(x,y)を出力する
print(gcd(x,y))