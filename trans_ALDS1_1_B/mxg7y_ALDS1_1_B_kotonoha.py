[#Document [# '! python3']][#Document [# 'greatest_common_divisor.py']]
# 関数greatest_common_divisorを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def greatest_common_divisor (x, y) :
  # 未定値をrとする
  r = None
  # xがy以上のとき、
  if x >= y :
    # xをyで割った余りをrとする
    r = x%y
    # rが0のとき、
    if r == 0 :
      # yを関数出力とする
      return y
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'r']expr: [#Infix left: [#Name 'y']name: [#Name '%']right: [#Name 'x']]][#If cond: [#Infix left: [#Name 'r']name: [#Name '==']right: [#Int '0']]then: [#Block [#Return expr: [#Name 'x']]]]]]
  # greatest_common_divisor(y,r)を関数出力とする
  return greatest_common_divisor(y, r)
# {{入力された文字列を' 'で分割した列}}の各要素をnとし、nの整数値の列を展開し順にxとyとする
x, y  = [int(n) for n in input().split(' ')]
# greatest_common_divisor(x,y)を出力する
print(greatest_common_divisor(x, y))