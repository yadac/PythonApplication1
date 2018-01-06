
# 型の宣言は不要
val = 100

# 代入演算可
# printでconsole出力
val += 100
print(val)

# 切り捨て除算
val = 10 // 3
print(val)

# 剰余
val = 10 % 3
print(val)

# 小数はfloat
val = 1 + 1.0
print(val)

# 3項演算
# 文字列はsingle quoteでくくる
# indexで文字列の切り出し可能
print('ok'[:1] if val > 0 else 'ng'[1:])

# 条件分岐
# オブジェクトの等価は is で判定する
#if (val > 100):
#	print("val is over 100")
#	print(val)
