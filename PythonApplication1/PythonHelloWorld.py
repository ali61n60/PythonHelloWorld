import sys 
from math import cos, radians

#def make_dot_string(x):
#    return ' ' * int(20 * cos(radians(x)) + 20) + 'o'


#for i in range(0,360,12) :
#     s = make_dot_string(i)
#     print(s)

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable)
myobjectx.function()