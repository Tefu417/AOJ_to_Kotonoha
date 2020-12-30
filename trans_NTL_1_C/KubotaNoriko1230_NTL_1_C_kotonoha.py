# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def gcd (a, b)  :
  # 真の間、繰り返す
  while True :
    # aがbより小さいとき、
    if a < b  :
      # aとbを入れ替える
      a, b = b, a
    # aをbで割った余りをamariとする
    amari = a % b
    # amariが0のとき、
    if amari == 0  :
      # 繰り返すのを中断する
      break
    # ()
    else :[#Else [#Block [#MultiAssignment left: [# [#Name 'a'][#Name 'b']]right: [#Tuple [#Name 'b'][#Name 'amari']]]]]
  # (b)の組を関数出力とする
  return (b)
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをcとする
c = list(map(int, input().split()))
# 'nから1を引いた値から0未満までの-1間隔の数列の各要素を順にiとして、繰り返す
for i  in range(n-1, 0, -1)  :
  # {{c(i)にc({{iから1を引いた値}})を掛けた値}}をgcd(c(i),c({{iから1を引いた値}}))で割った値の整数値をc[i-1] にする
  c[i-1]  = int(c[i] * c[i-1] / gcd(c[i], c[i-1]))
# cの最初値を出力する
print(c[0])