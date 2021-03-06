[#FromDecl name: [#ModuleName 'math']names: [# [#Name 'gcd']]]
## take amount of number
# 入力された文字列の整数値をaとする
a = int(input())  
## take all number in an array. Also can be solved without array in c++
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをbとする
b = list(map(int, input().split()))  
## assign first element to lcm
# b(0)をlcmとする
lcm = b[0]  
# bの先頭を除いた部分の各要素を順にmとして、繰り返す
for m  in b[1:] :
  ## check telegram tutorial to understand this
  # ({{lcmにmを掛けた値}})の組をgcd(lcm,m)で割った値の整数値をlcmとする
  lcm = int((lcm*m)/gcd(lcm, m))  
# lcmを出力する
print(lcm)