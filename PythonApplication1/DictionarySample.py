# Dictionary

# key-value pair
# 最後のカンマはあってもok
# keyの型は数値でもok
dict = {"k1":"v1"
		,"k2":"v2"
		,"k3":"v3"
		,1:False,}


print(dict["k2"])
print(dict[1])

dict1 = {"apple":"red", "grape":"purple", "banana":"yellow"}
# dict object is not callable.
# dict2 = dict(one=1, two=2, three=3)

print("apple" in dict1)
# print("zero" in dict2)

for key, val in dict1.items():
	print(key, val)

for key in dict1.keys():
	print(dict1[key])

