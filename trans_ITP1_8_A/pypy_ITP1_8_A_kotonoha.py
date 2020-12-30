# 入力された文字列の各要素を順にcとして、繰り返す
for c  in input() :
  # cの全てが英大文字のとき、
  if c.isupper() :
    # cを英小文字に変換した文字列と((end, ''))からなる辞書を出力する
    print(c.lower(), end='')
  # ('cの全てが英小文字の',)
  elif c.islower() :
    # cを英大文字に変換した文字列と((end, ''))からなる辞書を出力する
    print(c.upper(), end='')
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'c'][#Data [#KeyValue name: [#Name 'end']value: [#QString "''"]]]]]]]]
# 空行を出力する
print()