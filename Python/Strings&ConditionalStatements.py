str1 = "This is a String. we are creating it in python."
str4 = "This is a String.\nwe are creating it in python."
str5 = "This is a String.\twe are creating it in python."
str2 = 'Kishore Creates'
str3 = '''Hello World'''
a = "Apna"
b = "College"

# need for three different methods were to include ' and ".
# example 'this is apnacollege's tutorial.' [wrong.]
# example "This is apnacollege's tutorial." [Correct.]

print(str1)
print(str4)
print(str5)
print(a+b)
print(a + " " + b)
print(len(str2))
ch = str2[0]
print(ch)
# str2[0] = B  #Throws an error manipulation of string is not allowed

# Slicing
print(str2[1:5])  #final position is not included
print(str2[0:])
print(str2[:9])
print(str2[:-1])
print(str2[-9:-5])

# String Functions
str = "i am studying python from apnacollege"
print(str.endswith("ege"))
print(str.endswith("ing"))
#this will not change in og string will create a duplicate of it
print(str.capitalize())  
print(str) 
print(str.replace("o", "a"))
print(str.replace("python", "java"))
print(str.find("o"))
print(str.find("from"))
print(str.find("k"))
print(str.count("o"))
print(str.count("from"))
print(str.count("hello"))

# WAP to input user's first name and print its length.
str = input("Enter your first name: ")
print("Length: ", len(str))

# WAP to find the occurence of '$' in a string.
str = "Hello $ World $ How $ are You$"
print(str.count("$"))

# Conditional Statements
age =20
if(age >= 18):
    print("Can vote and apply for license.") #indentation
    print("Can drive and Drink.😅")
else:
    print("Sleep in Home.")

light = "green"
if(light == "red"): 
    print("Stop")
elif(light == "green"):
    print("Go")
elif(light == "yellow"):
    print("Ready") 
else: 
    print("Light is broken.")
print("End of code")

# Grade Students based on marks
marks = int(input("Enter the marks: "))
if(marks >= 90):
    print("A")
elif(marks >= 80):
    print("B")
elif(marks >= 70):
    print("C")
elif(marks >= 60):
    print("D")

# Nested If
age = 69
if(age >= 18):
    if(age >= 80):
        print("Cannot drive")
    else:
        print("Can Drive.")
else:
    print("cannot drive.")

# WAP to check if a number entered by the user is odd or even
num = int(input("Enter any positive number: "))
if(num%2 != 0):
    print("Odd")
else:
    print("Even")

#WAP to find the greatest of 3 numbers entered by the user.
num1 = int(input("Enter any positive number: "))
num2 = int(input("Enter any positive number: "))
num3 = int(input("Enter any positive number: "))
if(num1 > num2):
    if(num1 > num3):
        print(num1, "is the greatest among the three")
    elif(num3 > num1):
        print(num3, "is the greatest among the three")
elif(num2 > num3):
    print(num2, "is the greatest among the three")
else:
    print(num3, "is the greatest among the three")

# WAP to check if a number is a multiple of 7 or not.
num = int(input("Enter any positive number: "))
if(num%7 == 0):
    print(num, "is multiple of 7.")
else:
    print(num,"is not a multiple of 7.")