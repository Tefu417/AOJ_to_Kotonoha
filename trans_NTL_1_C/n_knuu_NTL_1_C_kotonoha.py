[#FromDecl name: [#ModuleName 'math']names: [# [#Name 'gcd']]]
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'arr']]]のパラメータを持つように定義する
def lcm (arr) :
  # 1をretとする
  ret = 1
  # arrの各要素を順にaとして、繰り返す
  for a  in arr :
    # retにaを掛けた値をgcd(ret,a)で割った商をretとする
    ret = ret * a // gcd(ret, a)
  # retを関数出力とする
  return ret
# 関数aojを[#FuncParam '()']のパラメータを持つように定義する
def aoj () :
  # 入力された文字列の整数値をNとする
  N = int(input())
  # lcm({{{{input()を空白で分割した列}}の各要素をxとし、xの整数値の列}})を出力する
  print(lcm([int(x) for x in input().split()]))
# 識別子が'__main__'のとき、
if __name__ == '__main__' :
  # aoj()
  aoj()