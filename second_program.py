#!/usr/bin/python3
a = 35
b = 65
try:
    c = a + b
    print("The value of c is: ", c)
    d = b / 0
    print("The value of d is: ", d)
    
except:
    print("Division by three is not possible")
    
    print("Out of try...except block")