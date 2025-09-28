# Lists
marks = [7.55, 6.59, 8.08, 7.75]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])

student = ["kishore", 7.55, 20, "Banglore"]
print(student[0])
student[1] = 8.15 #mutable
print(student)
# Slicing 
print(student[0: 2])

# List methods
# returns none but makes changes og list
list = [2,1,3]
print(list)
list.append(4)
print(list)
print(list.sort()) 
print(list)
(list.sort(reverse=True))
print(list)

list2 = [4, 5, 7, 8, 3, 4, 1]
print(list2)
list2.reverse()
print(list2)
list2.insert(1,18)
print(list2)
list2.remove(18) #removes first occurence of element
list2.pop(0) #removes elemrnt at index
print(list2)

# tuples
tup = (2, 1, 3, 1)
print(tup)
print(tup[0])
print(tup[1])
# tup[0] = 7 # Error

# Empty Tuple
tup1 = ()
print(tup1)
print(type(tup1))

# Single Value Tuple
tup2 = (18,) #comma is mandatory otherwise it will be considered as int.
print(tup2)
print(type(tup2))

tup3 = (10)
print(tup3)
print(type(tup3))

print(tup[1:3])

print(tup.count(1)) # counts total ocuurenence
print(tup.index(2)) # returns index of first occurence

#WAP to ask the user to eneter names of their 3 favorite movies & store them in a list
movies = []
print("Enter names of your 3 favorite movies: ")
movies.append(input())
movies.append(input())
movies.append(input())
print(movies)

# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
pal1 = [1,2,3,2,1]
pal2 = [1, "abc", "abc"]
pal1c = pal1.copy()
pal2c = pal2.copy()
pal1c.reverse()
pal2c.reverse()

if(pal1 == pal1c):
    print("Palindrome")
else:
    print("Not a Palindrome")

if(pal2 == pal2c):
    print("Palindrome")
else:
    print("Not a Palindrome")


# WAP to count the number of students with the "A" grade in the following tuple
grades = ("C", "D", "A", "A", "B", "B", "A")
print(grades.count("A"))

grades = ["C", "D", "A", "A", "B", "B", "A"]
grades.sort()
print(grades)