
list1 = ["foo", "bar"]
array1 = ("foo", "bar")
dictionary1 = {"a":"1","b":"2","c":"3",}
tuple1 = ("a", 1, False)

print("-----------------------")
print(len(list1))
print(len(array1))
print(len(dictionary1))
print(len(tuple1))
print("-----------------------")


print("foo", "bar")

# change default
print("foo", "bar", end = "\t", sep = ",")

# output to file
f = open("hoge.txt", "w", encoding="utf-8")
print("foobar", file=f)

print()
print("-----------------------")
# format output
print("%s-%s-%s" % ("foo", "bar", "piyo"))