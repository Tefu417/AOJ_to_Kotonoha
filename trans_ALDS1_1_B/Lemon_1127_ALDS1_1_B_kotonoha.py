# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a,b  = map(int,input().split())
# aがbより小さいとき、
if a < b :
  # aとbを入れ替える
  a, b = b, a
# bが0と等しくない間、繰り返す
while b != 0 :
  # aをbで割った余りをcとする
  c = a % b
  # bとcをaとbとする
  a,b  = b,c
# aを出力する
print(a)