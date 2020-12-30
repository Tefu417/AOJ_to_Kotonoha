# 関数gozyoを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def gozyo (x,y) :
  # 真の間、繰り返す
  while True :
    # yが0のとき、
    if y == 0 :
      # xを関数出力とする
      return x
    # xをyで割った余りをxとする
    x = x % y
    # xをzとする
    z = x
    # yをxとする
    x = y
    # zをyとする
    y = z
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a,b  = map(int,input().split())
# aがbより小さいとき、
if a < b :
  # aをcとする
  c = a
  # bをaとする
  a = b
  # cをbとする
  b = c
# gozyo(a,b)を出力する
print(gozyo(a,b))