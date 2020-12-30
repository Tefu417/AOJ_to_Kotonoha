# 入力された文字列の整数値をnとする
n = int(input())
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'a']]]のパラメータを持つように定義する
def lcm (a) :[#FromDecl name: [#ModuleName 'fractions']names: [# [#Name 'gcd']]]
  # aの最初値をxとする
  x = a[0]
  # '1からaの長さ未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(1, len(a)) :
    # ({{xにa(i)を掛けた値}})の組をgcd(x,a(i))で割った商をxとする
    x = (x * a[i]) // gcd(x, a[i])
  # xを関数出力とする
  return x
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# lcm(a)を出力する
print(lcm(a))