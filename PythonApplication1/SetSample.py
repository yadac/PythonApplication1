# set

# list, tupleと違って重複した値・順番の概念を持たない
s1 = {"hoge", 999, True}
print(s1)

# []で囲む意味はない、というか実行時エラーになる、誤植と理解
s2 = {"fuga", 100, False}
print(s2)

s3 = set("hogehoge")
print(s3)

# 出力順は保証されない

list1 = ["hoge", "fuga", "foo", "fuga", "foo"]

# merged duplicate value
sets = set(list1)
print(sets)

# set calculation
sets1 = {"a","b","c","d",}
sets2 = {"a", "c"}
print(sets1 - sets2)
print(sets1 & sets2)