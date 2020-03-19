# Python 3

# Why Python?

Python has a wide range of libraries for open-source data analysis tools, web frameworks, testing, and so on. Python is a programming language that can be used on different platforms (Windows, Mac, Linux, and embedded Linux H/W platforms, such as Raspberry Pi). It's used to develop desktop as well as web applications.
Developers can write programs with fewer lines if they use Python. Prototyping is very quick, as Python runs on an interpreter system. Python can be treated in an object-oriented, procedural, or functional way.
Python can do various tasks, such as creating web applications. It is used with the software to create workflows; it connects to database systems, handles files, handles big data, and performs complex mathematics.

The code written in Python is highly readable because it's similar to the English language. To complete a command, Python uses new lines.
Python has a great feature: indentation. Using indentations, we can define the scope for decision-making statements, loops such as for and while loops, functions, and classes.

## Python vs Bash

Python is a scripting language, whereas Bash is a shell used for entering and executing commands
Dealing with larger programs is easier with Python
In Python, you can do most things just by calling a one-line function from imported modules

# Variables and String

there's no need to declare your variables first. In Python, just think of any name to give your variable and assign it a value. You can use that variable in your program. So, in Python, you can declare variables whenever you need them.

Print()

age = 10
print("My age is %d " % age)

print("My age is %d %s %d" %(age, Years, 18))

f method
var1 = 20
var2 = vivek

print(f"This is my {var1} age")

print(f"This is my {0} age I am {1}".format(20, Vivek))
"""  """ for printing descriptions and Banners
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value


# Python Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	            Example

+       	Addition        	x + y	
-	        Subtraction	      x - y	
*       	Multiplication   	x * y	
/	        Division	        x / y	
%	        Modulus         	x % y	
**	      Exponentiation	  x ** y	
//	      Floor division	  x // y


Python Assignment Operators
Assignment operators are used to assign values to variables:

Operator	  Example	      Same As	
=         	x = 5	        x = 5	
+=	        x += 3	      x = x + 3	
-=	        x -= 3	      x = x - 3	
*=	        x *= 3	      x = x * 3	
/=	        x /= 3	      x = x / 3	
%=	        x %= 3	      x = x % 3	
//=	        x //= 3	      x = x // 3	
**=	        x **= 3	      x = x ** 3	
&=	        x &= 3	      x = x & 3	
|=	        x |= 3	      x = x | 3	
^=	        x ^= 3	      x = x ^ 3	
>>=	        x >>= 3       x = x >> 3	
<<=	        x <<= 3	      x = x << 3

# Data Types

Lists are enclosed in square brackets [ ] and they are mutable.

Tuples are enclosed in parentheses ( ) and they are immutable. 

A dictionary is a data type in Python, which consists of key-value pairs and is enclosed in curly braces { }. Dictionaries are unordered and indexed by keys, where each key must be unique. These keys must be immutable type. Tuples can be used as keys if they contain only strings, numbers, or tuples.

Set is a collection which is unordered and unindexed. No duplicate members. In Python sets are written with curly brackets{ }.

# Python Conditional Systems

Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

if Statements

a = 33
b = 200
if b > a:
  print("b is greater than a")
  

AND

if a > b and c > a:
  print("Both conditions are True")
  
OR

if a > b or c > a:
  print("Both conditions are True")
  
  
if else statements

if a > b:
  print("a is greater than b")
else:
  print("b is greater than a")

if elif else statments

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
Nested if else statement

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
    
The Pass Statement

a = 33
b = 200

if b > a:
  pass
  
# Python Loops
Python has two primitive loop commands:

while loops
for loops 

While loops

while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
  print(i)
  i += 1
  
break Statement

With the break statement we can stop the loop even if the while condition is true:  

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
continue Statement
With the continue statement we can stop the current iteration, and continue with the next

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  
break Statement
With the break statement we can stop the loop before it has looped through all the items:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
    
    
continue Statement
With the continue statement we can stop the current iteration of the loop, and continue with the next:    
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
  
  
  
range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for i in range(0,10):
  print(i)
  
Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)
  
  
  
Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
    
    
    
