# First Program
print("Hello World")
print("Kishore Gowda", "Kishore Creates")
print(18)
print(18+9)

# Variables
name = "Python"
value = "Good"
price = 69
lang = name
print(name)
print("Language : ", name)
print(price)
print(lang)

# DataType
print(type(name))
print(type(price))
old = False
a = None
print(type(old))
print(type(a))

# Different ways to to define
val1 = "Hey"
val2 = 'Hey'
val3 = '''Hey'''
print(val1)
print(val2)
print(val3)

# Quote Type	                    Primary Use
# Single ('...')	                For single-line strings, especially when the string contains ".
# Double ("...")	                For single-line strings, especially when the string contains '.
# Triple ('''...''' or """...""")	For multi-line strings and writing docstrings.

# Sum
x = 18
y = 9
sum = x + y
print(sum)

# Single Line Comment
"""
Multi
Line 
Comment 
"""

# Arithmetic operators
print(x + y)
print(x - y)
print(x * y)
print(x / y)  #always returns a floating value
print(x % y)  # Remainder
print(x ** y)  #x^y


# Relational/Comparison Operators
u = 50
v = 30

print(u == v)
print(u != v)
print(u > v)
print(u < v)
print(u >= v)
print(u <= v)

# Assignment Operator
num = 10
# num = num + 10
num += 10
print(num)
num -= 10
print(num)
num *= 10
print(num)
num /= 10
print(num)
num %= 10
print(num)
num **= 10
print(num)

# Logical Operators
print(not False)
print(not True)
print(not (x>y))

v1 = True
v2 = False
print(v1 and v2)
print(v1 or v2)

# Type Cpnversion
c = 2
d = 4.35

sum = c + d
print(sum)

# Type Casting
b = "2"
print(type(b))
# sum = b + c  # Error
sum = int(b) + c
print(sum)

# Input in Python
name = input("Enter your name: ")
print("Welcome", name)

val = input("Enter some value: ")
print(type(val))  # always String

typer = int(input("Enter Age: "))
print(typer)
print(type(typer))

# Lets Practice
# Write a program to input 2 numbers and print the sum
int1 = int(input("Enter 1st number: "))
int2 = int(input("Enter 2nd number: "))
sum = int1 + int2
print("Sum : ", sum )

# WAP to input side of a square and print its area
side = int(input("Enter the side of a square : "))
area = side*side
print("Area of the square : ", area)

# WAP to input 2 floating point numbers and print their average
flt1 = float(input("Enter 1st number: "))
flt2 = float(input("Enter 2nd number: "))
avg = (flt1 + flt2)/2
print("Average : ", avg )

# WAP to input 2 int numbers, a and b print True if a is greater than or equal to b. If not print False
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print(a>=b)

