
list1 = ["foo", "bar"]
array1 = ("foo", "bar")
dictionary1 = {"a":"1","b":"2","c":"3",}
tuple1 = ("a", 1, False)
set1 = {"b", 2, True}

print("-----------------------")
print(len(list1))
print(len(array1))
print(len(dictionary1))
print(len(tuple1))
print(len(set1))
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

print("-----------------------")
# min max
list2 = [1,2,3,4,5]
array2 = (1,2,3,4,5)
print(min(1,2,3,4,5))
print(max(array2))
print(max(list2))
print(min(dictionary1)) # sort by key

tuple2 = (2, 1, False)
# print(max(tuple1))  # str can not compare to integer
print(max(tuple2)) 

set2 = {0, 0.1, True}
print(max(set2)) # true is 1
