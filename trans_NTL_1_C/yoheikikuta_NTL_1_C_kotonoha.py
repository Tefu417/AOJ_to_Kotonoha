# copyモジュールを用いる
import copy
# mathモジュールを用いる
import math[#FromDecl name: [#ModuleName 'typing']names: [# [#Name 'List']]]
# 関数compute_prime_factorを[#FuncParam [#ParamDecl name: [#Name 'n']type: [#BaseType 'int']]]のパラメータを持つように定義する
def compute_prime_factor (n: int)  :[#Global [# [#Name 'prime_factors']]]
  # math.sqrt(n)の整数値に1を加えた値をsqrt_nとする
  sqrt_n = int(math.sqrt(n)) + 1
  # '2からsqrt_nに1を加えた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(2, sqrt_n + 1) :
    # 0が({{nをiで割った余り}})の組のとき、
    if 0 == (n % i) :
      # prime_factors.append(i)
      prime_factors.append(i)
      # compute_prime_factor(nをiで割った商)
      compute_prime_factor(n // i)
      # 関数処理を中断する
      return 
  # 1がnと等しくないとき、
  if 1 != n :
    # prime_factors.append(n)
    prime_factors.append(n)
    # 関数処理を中断する
    return 
# 識別子が"__main__"のとき、
if __name__ == "__main__" :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # 'map([#FuncExpr params: [#Param [#Name 'x']]body: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#Name 'x']]]],{{入力された文字列を空白で分割した列}})のリストをAとする
  A = list(map(lambda x: int(x), input().split()))
  # 空辞書をprime_factor_dictとする
  prime_factor_dict = {}
  # '0からn未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(n) :
    ## type: ignore
    # 空列をprime_factorsとする
    prime_factors = []  
    # compute_prime_factor(A(i))
    compute_prime_factor(A[i])
    # prime_factorsをprime_factor_dict[A[i]] にする
    prime_factor_dict[A[i]]  = prime_factors
  # Aの最大値をmax_numとする
  max_num = max(A)
  # prime_factor_dict(max_num)をall_factorsとする
  all_factors = prime_factor_dict[max_num]
  # prime_factor_dict.items()の各要素を順にkeyとfactorsとして、繰り返す
  for key, factors  in prime_factor_dict.items() :
    # keyがmax_num、またはkeyが1のとき、
    if key == max_num or key == 1 :
      # 最初からもう一度、繰り返す
      continue
    # copy.deepcopy(prime_factor_dict[max_num])をtmpとする
    tmp = copy.deepcopy(prime_factor_dict[max_num])
    # factorsの各要素を順にelemとして、繰り返す
    for elem  in factors :
      # elemがtmpに含まれるとき、
      if elem in tmp :
        # tmp.pop(tmp.index(elem))
        tmp.pop(tmp.index(elem))
      # ()
      else :[#Else [#Block [#Expression [#MethodExpr recv: [#Name 'all_factors']name: [#Name 'append']params: [#Arguments [#Name 'elem']]]]]]
  # 1をansとする
  ans = 1
  # all_factorsの各要素を順にelemとして、繰り返す
  for elem  in all_factors :
    # ([[#Name 'ans'], [#Name 'elem']],)
    [[#Name 'ans'], [#Name 'elem']]
  # ansを出力する
  print(ans)