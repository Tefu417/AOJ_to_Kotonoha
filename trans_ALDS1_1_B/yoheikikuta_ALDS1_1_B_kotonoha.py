# 関数find_gcdを[#FuncParam [#ParamDecl name: [#Name 'a']type: [#BaseType 'int']][#ParamDecl name: [#Name 'b']type: [#BaseType 'int']]]のパラメータを持つように定義する
def find_gcd (a: int, b: int)  :
  # aがbより小さいとき、
  if a < b :
    # aとbを入れ替える
    a, b = b, a
  # bが0のとき、
  if b == 0 :
    # aを関数出力とする
    return a
  # find_gcd(b,aをbで割った余り)を関数出力とする
  return find_gcd(b, a % b)
# 識別子が"__main__"のとき、
if __name__ == "__main__" :
  # 'map([#FuncExpr params: [#Param [#Name 'x']]body: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#Name 'x']]]],{{入力された文字列を空白で分割した列}})のリストを展開し順にaとbとする
  a, b  = list(map(lambda x: int(x), input().split()))
  # [#Format [#ApplyExpr name: [#Name 'find_gcd']params: [#Arguments [#Name 'a'][#Name 'b']]]]を出力する
  print(f"{find_gcd(a, b)}")