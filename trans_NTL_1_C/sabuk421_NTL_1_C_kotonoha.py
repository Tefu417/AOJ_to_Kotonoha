# mathモジュールを用いる
import math
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# 'aの集合のリストをa_sとする
a_s = list(set(a))
# a_sの長さが1と等しくない間、繰り返す
while len(a_s)!=1 :
  # math.gcd(a_s[-1],a_s[-2])をgcdとする
  gcd = math.gcd(a_s[-1],a_s[-2])
  # {{a_sの末尾値にa_s(-2)を掛けた値}}をgcdで割った値の整数値をlcmとする
  lcm = int(a_s[-1]*a_s[-2]/gcd)
  # a_sの位置先頭から位置-2までの部分をa_sとする
  a_s = a_s[:-2]
  # a_s.append(lcm)
  a_s.append(lcm)
# a_sの最初値を出力する
print(a_s[0])