# exception

try:
	x = 10 / 0
except Exception as e:
	print(e) # division by zero
else:
	# exception does not raise
	print("any exceptions had not raised.")
finally:
	print("finally fuga") # fuga

try:
	raise Exception("hoge")
except Exception as e:
	print(e) # hoge

def hogehoge():
	pass