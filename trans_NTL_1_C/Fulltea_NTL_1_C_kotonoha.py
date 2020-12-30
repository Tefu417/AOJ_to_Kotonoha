# 入力された文字列の整数値をnとする
n = int(input())
# 関数GCDを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def GCD (a,b) :
  # aとbの最小値が0のとき、
  if min(a,b)==0 :
    # aとbの最大値を関数出力とする
    return max(a,b)
  # ()
  else :[#Else [#Block [#Return expr: [#ApplyExpr name: [#Name 'GCD']params: [#Arguments [#ApplyExpr name: [#Name 'min']params: [#Arguments [#Name 'a'][#Name 'b']]][#Infix left: [#ApplyExpr name: [#Name 'max']params: [#Arguments [#Name 'a'][#Name 'b']]]name: [#Name '%']right: [#ApplyExpr name: [#Name 'min']params: [#Arguments [#Name 'a'][#Name 'b']]]]]]]]]
# 関数LCMを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def LCM (a,b) :
  # ({{aにbを掛けた値}})の組をGCD(a,b)で割った商を関数出力とする
  return (a*b)//GCD(a,b)
# {{入力された文字列を" "で分割した列}}の各要素をiとし、iの整数値の列をaとする
a = [int(i) for i in input().split(" ")]
# 1をlcmとする
lcm = 1
# aの各要素を順にaiとして、繰り返す
for ai  in a :
  # LCM(ai,lcm)をlcmとする
  lcm = LCM(ai,lcm)
# lcmを出力する
print(lcm)