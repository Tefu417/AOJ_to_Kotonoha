# 関数gを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def g (a, b) :
  # bの間、繰り返す
  while b :
    # bとaをbで割った余りをaとbとする
    a, b  = b, a%b
  # aを関数出力とする
  return a
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int, input().split()))
# aの最初値にa(1)を掛けた値をg(aの最初値,a(1))で割った値をansとする
ans = a[0]*a[1]/g(a[0],a[1])
# aの先頭2個を取り除いた部分の各要素を順にiとして、繰り返す
for i  in a[2:] :
  # ansにiを掛けた値をg(ans,i)で割った値をansとする
  ans = ans*i/g(ans,i)
# ansの整数値を出力する
print(int(ans))