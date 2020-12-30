# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def gcd (a,b) :
  # bが0のとき、
  if b == 0 :
    # aを関数出力とする
    return a
  # gcd(b,aをbで割った余り)を関数出力とする
  return gcd(b,a%b)
# 関数mainを[#FuncParam '()']のパラメータを持つように定義する
def main () :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
  a,b  = map(int,input().split())
  # aがbより小さいとき、
  if a<b :
    # aとbを入れ替える
    a, b = b, a
  # gcd(a,b)を出力する
  print (gcd(a,b))
# 識別子が'__main__'のとき、
if __name__ == '__main__' :
  # main()
  main()