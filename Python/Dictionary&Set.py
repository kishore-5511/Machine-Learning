# Dictionares in python
info = {
    "name" : "apnacollege",
    "subjects" : ["python", "C", "Java"],
    "topics" : ("dict", "set"),
    "age" : 20,
    "is_adult" : True,
    3 : 7.51
}
# keys can be string, integer, float, boolean, tuple anything which are immutable

print(type(info))
print(info)
print(info["name"])
info["name"] = "Kishore Gowda"
info["Gym"] = True
print(info)

# null dictionary
null_dict = {}
print(null_dict)
print(type(null_dict))

#nested Dictionay
student = {
    "name" : "Kishore Gowda",
    "subjects" : {
        "1st year" : 7.07,
        "2nd year" : 7.51
    }
}

print(student["subjects"])
print(student["subjects"]["2nd year"])

# Dictionary Methods
print(student.keys()) # returns all keys
print(list(student.keys())) # Type casted to list
print(len(student))
print(student.values()) # returns all values
print(student.items()) #  returns all (key, val) pairs in tuple

print(student["name"])
print(student.get("name"))

# print(student["name2"])  #Error
print(student.get("name2"))  # No Error returns none

student.update({"age" : 20, "City" : "Bengaluru"})
print(student)

# Sets in Python
collection = {1,2,2,2,"hello", "World", "World"} # duplicates are ignored
print(collection)
print(type(collection))
print(len(collection))  #number of unique elements

collection1 = {} #empty dictionary syntax
collection2 = set() # empty set

print(type(collection1))
print(type(collection2))

# set Methods
collection.add("kishore")
collection.add(18)
collection.add((18, 3, 2005))
print(collection)

collection.remove("hello")
collection.remove(1)
collection.remove(2)
print(collection)

# collection.clear() #empties the set

print(collection.pop())
print(collection)

set1 = {1,2,3}
set2 = {3,4,5}

# this methods create a new set doesnt affect the og set
print(set1.union(set2))
print(set1.intersection(set2))

#Store following words meaning in python dictionary:
meaning = {
    "table" : ["a piecae of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}
print(meaning)

# you are given a list of subkkkects for students. Assume one classroom is required for 1 sudject. How many classrooms are needed by all students

classroom = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(classroom))

#WAP to enter marks of 3 subjects from the user and store them in a dictonary. Start with an empty dictionary and add one by one. Use subject name as key & marks as value.

store = {}
x = int(input("Enter Phy Marks: "))
store.update({"phy" : x})
x = int(input("Enter chem Marks: "))
store.update({"chem" : x})
x = int(input("Enter math Marks: "))
store.update({"math" : x})
print(store)

#Figure out a way to store 9 and 9.0 as seperate values in the set.
values = {9, 9.0} # it works based on hashing
print(values)

values1 = {9, "9.0"} 
print(values1)

values1 = {
    ("int", 9),
    ("float", 9.0)
}
print(values1)