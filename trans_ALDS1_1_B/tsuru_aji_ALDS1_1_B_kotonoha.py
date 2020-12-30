# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def gcd (x,y) :
  # xがyより小さいとき、
  if x < y :
    # xとyを入れ替える
    x, y = y, x
  # yが0より大きい間、繰り返す
  while y > 0 :
    # xをyで割った余りをrとする
    r = x % y
    # yをxとする
    x = y
    # rをyとする
    y = r
  # xを出力する
  print(x)
# map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
x,y  = map(int,input().split())
# gcd(x,y)
gcd(x,y)