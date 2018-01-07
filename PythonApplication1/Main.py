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


import calendar
print("------------------")
print(calendar.month(1999,12))