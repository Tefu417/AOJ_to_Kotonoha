# 入力された文字列の文字列をwとする
w = str(input())
# ""をansとする
ans = ""
# wの各要素を順にcとして、繰り返す
for c  in w :
  # 96がcの順序数より小さいかどうかが123より小さいとき、
  if 96<ord(c)<123 :
    # cを英大文字に変換した文字列をcとする
    c = c.upper()
  # ([[#Name 'ans'], [#Name 'c']],)
  [[#Name 'ans'], [#Name 'c']]
# ansを出力する
print(ans)