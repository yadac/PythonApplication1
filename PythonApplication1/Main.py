# import Sub.py
# don't need extension
import Sub

Sub.printer("hello world")

# module exists the other directory 
#from subdir import Sub2
#Sub2.subFnc()

#import subdir.Sub2
#subdir.Sub2.subFnc()

# import package1 means, read __init__.py setting.
import package1
package1.Sub1.subFnc()
package1.Sub2.subFnc()


# external library
# normally install library from PyPI.
import calendar
print("------------------")
print(calendar.month(1999,12))

val = 100

def fuc():
	val = 1 # local scope
	print(val)

def fuc2():
	print(val) # module scope

fuc()
fuc2()
print(val)

if True:
	val = 999

print(val)

import Member
member = Member.Member()
member.setName("taro")
print(member.getName()) # taro
print(member.LANG)