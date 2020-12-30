[#Document [# 'coding=utf-8']]
# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'n1']][#ParamDecl name: [#Name 'n2']]]のパラメータを持つように定義する
def gcd (n1, n2) :
  # n1がn2より小さいとき、
  if n1 < n2 :
    # n1とn2を入れ替える
    n1, n2 = n2, n1
  # n1がn2、またはn2が0のとき、
  if n1 == n2 or n2 == 0 :
    # n1を関数出力とする
    return n1
  # n2と(n1をn2で割った余り)の組をn1とn2とする
  n1, n2  = n2, (n1 % n2)
  # gcd(n1,n2)を関数出力とする
  return gcd(n1, n2)
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'n1']][#ParamDecl name: [#Name 'n2']]]のパラメータを持つように定義する
def lcm (n1, n2) :
  # n1にn2を掛けた値をgcd(n1,n2)で割った商を関数出力とする
  return n1*n2//gcd(n1, n2)
# 関数multi_lcmを[#FuncParam [#ParamDecl name: [#Name 'numbers_list']]]のパラメータを持つように定義する
def multi_lcm (numbers_list) :
  # numbers_listの長さが2のとき、
  if len(numbers_list) == 2 :
    # lcm(numbers_listの最初値,numbers_list(1))を関数出力とする
    return lcm(numbers_list[0], numbers_list[1])
  # ('numbers_listの長さが2より大きい',)
  elif len(numbers_list) > 2 :
    # (lcm(numbers_listの最初値,numbers_list(1)))からなる列をnumbers_list2とする
    numbers_list2 = [lcm(numbers_list[0], numbers_list[1])]
    # numbers_list2.extend(numbers_list[2:])
    numbers_list2.extend(numbers_list[2:])
    # multi_lcm(numbers_list2)を関数出力とする
    return multi_lcm(numbers_list2)
# 識別子が'__main__'のとき、
if __name__ == '__main__' :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをnumber_listとする
  number_list = list(map(int, input().split()))
  # multi_lcm(number_list)を出力する
  print(multi_lcm(number_list))