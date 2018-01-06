
# programming flow
v1 = 1
v2 = 2
v3 = 3

print("------------------- condition")

# if condition, does not need "end"
if v1 == v2:
	print("v1 == v2")
elif v1 > v2:
	print("v1 > v2")
else:
	print("v2 > v1")

# like switch statement
if v3 == 1:
	print("v3 == 1")
elif v3 in (2, 3):
	print("v3 in (2, 3)")
elif v3 in (3, 4):
	print("v3 in (3, 4)")
else:
	print("else")


# loop
# for(=foreach) + range / while
# use break keyword for end loop

print("------------------- while")
while v1 < 3:
	print(v1)
	v1 += 1

v1 = 1 # initialize

print("------------------- for with range")
for i in range(2):
	print(i)

print("------------------- for with list")
l1 = [100, False, "hello"]
for i in l1:
	print(i)

print("------------------- for with string")
for i in l1[2]:
	print(i)

