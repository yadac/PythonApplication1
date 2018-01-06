# Function

# b has default value as 1
def calc(a, b = 1):
	return a + b

# not return value
def originalPrinter(a):
	print(a)

# call function
# indicates args name with value, ignore order
print(calc(1))
print(calc(1, 2))
print(calc(b = 3, a = 10))
print("hello world")

# b is memoried, scope is not function
def listContain(a, b = []):
	b.append(a)
	return b

# if you want to do not memory, use "None" keyword
def listContain2(a, b = None):
	if b is None:
		print("b is None")
		b = []
	b.append(a)
	return b

# python is everything "byref"
print(listContain(0))
print(listContain(0))
print(listContain(0))
print(listContain(0, [1, 2]))

print(listContain2(0))
print(listContain2(0))
print(listContain2(0))
print(listContain2(0, [1, 2]))
