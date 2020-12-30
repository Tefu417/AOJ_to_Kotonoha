# map(整数,入力された文字列を空白で分割した列)を展開し順にnとmとする
n,m  = map(int,input().split())
# nがmより小さいとき、
if n < m :
  # nとmを入れ替える
  n, m = m, n
# nをmで割った余りが0と等しくない間、繰り返す
while n % m !=0 :
  # mとnをmで割った余りをnとmとする
  n,m  = m,n%m
# mを出力する
print(m)