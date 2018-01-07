# Tuple

# listのようにindexでアクセス
# listと異なり要素の変更は不可
t1 = ("hoge", 999, False)
print(t1[1])

t2 = ("fuga",)
print(t2[0])

key1 = ("masaru", "10-18")
key2 = ("manabu", "05-01")

dict = {key1:38, key2:25}
print(dict)

# return multiple value
def getABC():
	return ("A", "B", "C")

(a,b,c) = getABC()

print(a)
print(b)
print(c)