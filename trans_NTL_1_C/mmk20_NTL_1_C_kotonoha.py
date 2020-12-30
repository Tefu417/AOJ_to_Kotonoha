[#Document [# '76 最小公倍数']]
# mathモジュールを用いる
import math
# 関数mainを[#FuncParam [#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def main (n) :
  # 1をansとする
  ans = 1
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをlstとする
  lst = list(map(int, input().split()))
  # lstの各要素を順にiとして、繰り返す
  for i  in lst :
    # ansにiを掛けた値をmath.gcd(ans,i)で割った商をansとする
    ans = ans * i // math.gcd(ans,i)
  # ansを出力する
  print(ans)
# main(入力された文字列の整数値)
main(int(input()))