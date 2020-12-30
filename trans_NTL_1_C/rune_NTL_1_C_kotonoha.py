# 関数calc_gcdを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def calc_gcd (x, y) :
  # xがyより小さいとき、
  if x < y :
    # xとyを入れ替える
    x, y = y, x
  # yが0より大きい間、繰り返す
  while y > 0 :
    # yとxをyで割った余りをxとyとする
    x, y  = y, x % y
  # xを関数出力とする
  return x
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをAとする
A = list(map(int, input().split()))
# 未定値をa_lastとする
a_last = None
# Aの各要素を順にaとして、繰り返す
for a  in A :
  # a_lastが未定値のとき、
  if a_last == None :
    # aをa_lastとする
    a_last = a
    # 最初からもう一度、繰り返す
    continue
  # calc_gcd(a,a_last)をgcdとする
  gcd = calc_gcd(a, a_last)
  # aにa_lastを掛けた値をgcdで割った値をa_lastとする
  a_last = a * a_last / gcd
# a_lastの整数値を出力する
print(int(a_last))