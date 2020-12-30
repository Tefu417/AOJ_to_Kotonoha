# 関数toggleを[#FuncParam [#ParamDecl name: [#Name 's']]]のパラメータを持つように定義する
def toggle (s) :
  # [#MultiString '"Return a copy of the string with uppercase characters\n    converted to lowercase and vice versa.\n\n    >>> toggle("fAIR, LATER, OCCASIONALLY CLOUDY.")\n    \'Fair, later, occasionally cloudy.\'\n    "']
  "Return a copy of the string with uppercase characters
    converted to lowercase and vice versa.

    >>> toggle("fAIR, LATER, OCCASIONALLY CLOUDY.")
    'Fair, later, occasionally cloudy.'
    "
  # sの英大文字を英小文字、英小文字を英大文字に変換した文字列を関数出力とする
  return s.swapcase()
# 関数runを[#FuncParam '()']のパラメータを持つように定義する
def run () :
  # toggle(入力された文字列)を出力する
  print(toggle(input()))
# run()
run()