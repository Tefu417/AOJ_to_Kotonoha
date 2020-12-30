# 識別子が"__main__"のとき、
if __name__ == "__main__" :
  # 入力された文字列をinput_strとする
  input_str = input()
  # ({{{{sの全てが英小文字の}}とき{{sを英大文字に変換した文字列}}、そうでなければ{{input_strの各要素をsとし、s.lower() の列}}}})からなる列を文字列""で連結した文字列を出力する
  print("".join([s.upper() if s.islower() else s.lower() for s in input_str]))