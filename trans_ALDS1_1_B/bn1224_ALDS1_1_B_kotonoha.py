# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# aがbより小さいとき、
if a < b :
  # aとbを入れ替える
  a, b = b, a
# aをbで割った余りが0と等しくない間、繰り返す
while a % b != 0 :
  # bとaをbで割った余りをaとbとする
  a, b  = b, a % b
# bを出力する
print(b)