# import Sub.py
# don't need extension
import Sub

Sub.printer("hello world")

# module exists the other directory 
from subdir import Sub2
Sub2.print2("python world")

import subdir.Sub2
subdir.Sub2.print2("more python world")