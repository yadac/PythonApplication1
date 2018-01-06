
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

# 複素数
c1 = 1 + 1j
c2 = 1 - 2j
print(c1 + c2) #(2-1j)
print(c1 * c2) #(3-1j)

# bool false is 0, true is 1
print(True + 1)
print(False + 1)

# 3項演算
# 文字列はsingle/double quoteでくくる
# indexで文字列の切り出し可能
print('ok'[:1] if val > 0 else 'ng'[1:])

# 条件分岐
# オブジェクトの等価は is で判定する
#if (val > 100):
#	print("val is over 100")
#	print(val)
