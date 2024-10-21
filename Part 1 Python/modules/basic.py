import math
print(math.sqrt(9)) 


from math import sqrt, pi
print(sqrt(9))


# to include all functions and variables this is not recommended, will lead to confusion
from math import * 


import math as mt
# to import as separate name 
print(mt.sqrt(9))


# to show all things fxn and var that are exported from math module dir(module name)
# will work when import module name 
# print(dir(math)) 


from demo import welcome, me 
# print(dir(demo))
print(welcome())
print(me)