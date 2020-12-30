[#FromDecl name: [#ModuleName 'string']names: [# [#Name 'ascii_lowercase'][#Name 'ascii_uppercase']]]
# ascii_lowercaseをlとする
l = ascii_lowercase
# ascii_uppercaseをuとする
u = ascii_uppercase
# 関数convを[#FuncParam [#ParamDecl name: [#Name 'c']]]のパラメータを持つように定義する
def conv (c) :
  # cがlに含まれるとき、
  if c in l :
    # u(l.index(c))を関数出力とする
    return u[l.index(c)]
  # cがuに含まれるとき、
  if c in u :
    # l(u.index(c))を関数出力とする
    return l[u.index(c)]
  # cを関数出力とする
  return c
# open(1, 'w').write("".join(map(conv, open(0).readline())))
open(1, 'w').write("".join(map(conv, open(0).readline())))