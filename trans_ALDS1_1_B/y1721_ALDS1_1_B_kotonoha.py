# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def gcd (a, b) :
  # [#MultiString '"calculate the greatest common divisor of a, b\n\n    >>> gcd(54, 20)\n    2\n    >>> gcd(147, 105)\n    21\n    >>> gcd(100000002, 39273000)\n    114\n    "']
  "calculate the greatest common divisor of a, b

    >>> gcd(54, 20)
    2
    >>> gcd(147, 105)
    21
    >>> gcd(100000002, 39273000)
    114
    "
  # aがbより大きいとき、
  if a > b :
    # aとbを入れ替える
    a, b = b, a
  # aが0のとき、
  if a == 0 :
    # bを関数出力とする
    return b
  # gcd(bをaで割った余り,a)を関数出力とする
  return gcd(b % a, a)
# 関数runを[#FuncParam '()']のパラメータを持つように定義する
def run () :
  # {{入力された文字列を空白で分割した列}}の各要素をiとし、iの整数値の列を展開し順にaとbとする
  a, b  = [int(i) for i in input().split()]
  # gcd(a,b)を出力する
  print(gcd(a, b))
# 識別子が'__main__'のとき、
if __name__ == '__main__' :
  # run()
  run()