# mathモジュールを用いる
import math[#FromDecl name: [#ModuleName 'typing']names: [# [#Name 'List']]][#FromDecl name: [#ModuleName 'functools']names: [# [#Name 'reduce']]]
# 関数least_common_multipleを[#FuncParam [#ParamDecl name: [#Name 'x']type: [#BaseType 'int']][#ParamDecl name: [#Name 'y']type: [#BaseType 'int']]]のパラメータを持つように定義する
def least_common_multiple (x: int, y: int)  :
  # xにyを掛けた値をmath.gcd(x, y)で割った商を関数出力とする
  return x * y // math.gcd(x, y)
# 関数least_common_multiple_of_numbersを[#FuncParam [#ParamDecl name: [#Name 'numbers']type: [#ParamType [#BaseType 'List'][#BaseType 'int']]]]のパラメータを持つように定義する
def least_common_multiple_of_numbers (numbers: List[int])  :
  # numbersの長さが1のとき、
  if len(numbers) == 1 :
    # numbersの最初値を関数出力とする
    return numbers[0][#Document [# 'while len(numbers) != 1:'][# 'new_nums = []'][# 'for i in range(len(numbers) // 2):'][# 'new_nums.append(least_common_multiple(numbers[2*i], numbers[2*i+1]))'][# 'if len(numbers) % 2 != 0:'][# 'new_nums.append(numbers[-1])'][# 'numbers = new_nums'][# 'return numbers']]
  # reduce(least_common_multiple,numbers)を関数出力とする
  return reduce(least_common_multiple, numbers)
# 関数mainを[#FuncParam '()']のパラメータを持つように定義する
def main () :
  # 入力された文字列の整数値をmとする
  m = int(input())
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをnumbersとする
  numbers = list(map(int, input().split()))
  # least_common_multiple_of_numbers(numbers)をgcmとする
  gcm = least_common_multiple_of_numbers(numbers)
  # gcmを出力する
  print(gcm)
  # 関数処理を中断する
  return 
# main()
main()