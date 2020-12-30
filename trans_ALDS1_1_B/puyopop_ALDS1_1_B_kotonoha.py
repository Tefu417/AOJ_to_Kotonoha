# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def gcd (x, y) :
  # xがyより小さいとき、
  if x < y :
    # xとyを入れ替える
    x, y = y, x
  # yが0と等しくない間、繰り返す
  while y != 0 :
    # yとxをyで割った余りをxとyとする
    x, y  = y, x % y
  # xを関数出力とする
  return x
# 識別子が"__main__"のとき、
if __name__ == "__main__" :
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストを展開し順にxとyとする
  x, y  = list(map(int, input().split()))
  # gcd(x,y)を出力する
  print(gcd(x, y))