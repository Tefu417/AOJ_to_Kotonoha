# mathモジュールを用いる
import math
# 関数keisanを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def keisan (x,y) :
  # ({{xの最初値にx(1)を掛けた値}})の組をmath.gcd(x[0],x[1])で割った商をzとする
  z = (x[0]*x[1])//math.gcd(x[0],x[1])
  # '0からyから2を引いた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(y-2) :
    # ({{zにx({{iに2を加えた値}})を掛けた値}})の組をmath.gcd(z,x[i+2])で割った商をzとする
    z = (z*x[i+2])//math.gcd(z,x[i+2])
  # zを関数出力とする
  return z
# 入力された文字列の整数値をnとする
n = int(input())    
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# keisan(a,n)を出力する
print(keisan(a,n))