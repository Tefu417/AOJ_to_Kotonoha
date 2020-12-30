# map(整数,入力された文字列を空白で分割した列)を展開し順にNとMとする
N, M  = map(int, input().split())
# 真の間、繰り返す
while True :
  # NがMより小さいとき、
  if N < M  :
    # NとMを入れ替える
    N, M = M, N
  # NをMで割った余りをaとする
  a = N % M
  # aが0のとき、
  if a == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#MultiAssignment left: [# [#Name 'N'][#Name 'M']]right: [#Tuple [#Name 'M'][#Name 'a']]]]]
# Mを出力する
print(M)