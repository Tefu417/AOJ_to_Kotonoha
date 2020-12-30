# 入力された文字列の整数値をnとする
n = int(input())
# map(整数,入力された文字列を空白で分割した列)をaとする
a = map(int, input().split())
# a.__next__()をresultとする
result = a.__next__()
# aの各要素を順にnbとして、繰り返す
for nb  in a :
  # resultをnaとする
  na = result
  # ([[#Name 'result'], [#Name 'nb']],)
  [[#Name 'result'], [#Name 'nb']]
  # nbが0より大きい間、繰り返す
  while nb > 0 :
    # nbとnaをnbで割った余りをnaとnbとする
    na, nb  = nb, na%nb
  # ([[#Name 'result'], [#Name 'na']],)
  [[#Name 'result'], [#Name 'na']]
# resultを出力する
print(result)