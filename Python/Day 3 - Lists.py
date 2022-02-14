# Arrays aka lists
"""
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(weekdays)

MonList = ["Vegetables", "Fruit", "Bread", "Eggs"]
print(MonList)
WedList = ["Bread", "Eggs", "Mozarella", "Canned Tomatoes", "Yeast", "Flour"]
print(MonList)
FriList = ["Vegetables", "Eggs", "Bread", "Toilet Paper"]
print(FriList)

days = input("What day is it today?: ")

if days == "Monday":
    print("Here is todays shopping list: " + str(MonList))
elif days == "Wednesday":
    print("Here is todays shopping list: " + str(WedList))
elif days == "Friday":
    print("Here is todays shopping list: " + str(FriList))
else:
    print("You do not need to go shopping today")
    pass

#Python can create lists that include integers and strings
Horses = [1, "Gerry Klaferty", "Off to the races", 2]
print(Horses)

#Here is the code how access a specific position in a list
Pos = int(input("Which position"))
print(weekdays[Pos])
"""
"""
#Can also use the range funtion to generate lists
Numbers = list(range(16))
print(Numbers)
#
Numbers2 = list(range(5,26))
print(Numbers2)
#^creates and prints a list ranging from 5 to 26
Numbers3 = list(range(0,21,2))
print(Numbers3)
#^creates and prints a range between 0 and 21, but only in increments of 2
#You can check for the lengths of lists with the help of the len() function
C = len(Numbers)
print(C)


r1 = list(range(0,50))
print("1: 0,50")
r2 = list(range(0,100))
print("2: 0,100")
r3 = list(range(0,150))
print("3: 0,150")
r4 = list(range(0,200))
print("4: 0,200")

ruler = int(input("Which length of ruler would you like to select?: "))

if ruler == 1:
    print(str(r1))
elif ruler == 2:
    print(str(r2))
elif ruler == 3:
    print(str(r3))
elif ruler == 4:
    print(str(r4))
else:
    print("That is not a valid selection")
pass
"""

"""
# Exercise 10: Skipping parts with range
import random
import time

print("List number 1")
a=random.randint(1,50)
print("lower bound is "+str(a))
time.sleep(1)
b=random.randint(50,100)
print("upper bound is "+str(b))
time.sleep(1)
c=random.randint(1,10)
print("in increments of "+str(c))
time.sleep(1)

d1=list(range(a,b,c))
print(d1)
time.sleep(3)

print("List number 2")
a=random.randint(1,50)
print("lower bound is "+str(a))
time.sleep(1)
b=random.randint(50,100)
print("upper bound is "+str(b))
time.sleep(1)
c=random.randint(1,10)
print("in increments of "+str(c))
time.sleep(1)

d2=list(range(a,b,c))
print(d2)
time.sleep(3)

print("List number 3")
a=random.randint(1,50)
print("lower bound is "+str(a))
time.sleep(1)
b=random.randint(50,100)
print("upper bound is "+str(b))
time.sleep(1)
c=random.randint(1,10)
print("in increments of "+str(c))
time.sleep(1)

d3=list(range(a,b,c))
print(d3)
time.sleep(3)

print("So here are the 3 ranges")
time.sleep(1)
print(d1)
time.sleep(1)
print(d2)
time.sleep(1)
print(d3)
time.sleep(1)
"""

"""
# Elongation of lists

list1 = list(range(4))
list2 = list(range(5))
print(list1)
print(list2)

list1.append(list2)
print(list1)
#append function created a multi dimensional list aka a list within a list e.g. types of oranges (list) within a shopping list (list).

print(len(list1))

print(list1[4])

list1.append(5)

list3 = list(range(5))
list1.extend(list3)
print(list1)


List = ["Apples", "Pears", "Oranges", "Peaches"]
print(List)

List5=list(range(5))
print(List5)

List.append(List5)
print(List)

# Exercise 11 - Longer lists

import random
import time

print("List number 1")
a=random.randint(1,50)
print("lower bound is "+str(a))
time.sleep(1)
b=random.randint(50,100)
print("upper bound is "+str(b))
time.sleep(1)
c=random.randint(1,10)
print("in increments of "+str(c))
time.sleep(1)

d1=list(range(a,b,c))
print(d1)
time.sleep(1)

print("List number 2")
a=random.randint(1,50)
print("lower bound is "+str(a))
time.sleep(1)
b=random.randint(50,100)
print("upper bound is "+str(b))
time.sleep(1)
c=random.randint(1,10)
print("in increments of "+str(c))
time.sleep(1)

d2=list(range(a,b,c))
print(d2)
time.sleep(1)

print("List number 3")
a=random.randint(1,50)
print("lower bound is "+str(a))
time.sleep(1)
b=random.randint(50,100)
print("upper bound is "+str(b))
time.sleep(1)
c=random.randint(1,10)
print("in increments of "+str(c))
time.sleep(1)

d3=list(range(a,b,c))
print(d3)
time.sleep(1)

print("List number 4")
a=random.randint(1,50)
print("lower bound is "+str(a))
time.sleep(1)
b=random.randint(50,100)
print("upper bound is "+str(b))
time.sleep(1)
c=random.randint(1,10)
print("in increments of "+str(c))
time.sleep(1)

d4=list(range(a,b,c))
print(d4)
time.sleep(1)

print("List number 5")
a=random.randint(1,50)
print("lower bound is "+str(a))
time.sleep(1)
b=random.randint(50,100)
print("upper bound is "+str(b))
time.sleep(1)
c=random.randint(1,10)
print("in increments of "+str(c))
time.sleep(1)

d5=list(range(a,b,c))
print(d5)
time.sleep(1)

print("List number 6")
a=random.randint(1,50)
print("lower bound is "+str(a))
time.sleep(1)print("List number 1")
a=random.randint(1,50)
print("lower bound is "+str(a))
time.sleep(1)
b=random.randint(50,100)
print("upper bound is "+str(b))
time.sleep(1)
c=random.randint(1,10)
print("in increments of "+str(c))
time.sleep(1)

d1=list(range(a,b,c))
print(d1)
time.sleep(1)

print("List number 2")
a=random.randint(1,50)
print("lower bound is "+str(a))
time.sleep(1)
b=random.randint(50,100)
print("upper bound is "+str(b))
time.sleep(1)
c=random.randint(1,10)
print("in increments of "+str(c))
time.sleep(1)

d2=list(range(a,b,c))
print(d2)
time.sleep(1)
b=random.randint(50,100)
print("upper bound is "+str(b))
time.sleep(1)
c=random.randint(1,10)
print("in increments of "+str(c))
time.sleep(1)

d6=list(range(a,b,c))
print(d6)
time.sleep(1)


print("So here are the 6 lists")
time.sleep(1)
print(d1)
time.sleep(1)
print(d2)
time.sleep(1)
print(d3)
time.sleep(1)
print(d4)
time.sleep(1)
print(d5)
time.sleep(1)
print(d6)
time.sleep(1)

#Append the third list to the first one
print("Append the third list to the first one")
time.sleep(2)
d1.append(d3)
print(d1)
time.sleep(2)
#Append the fourth list to the second one
print("Append the fourth list to the second one")
time.sleep(2)
d2.append(d4)
print(d2)
time.sleep(2)
#Extend the first list with the fifth list
print("Extend the first list to the fifth one")
time.sleep(2)
d1.extend(d5)
print(d1)
time.sleep(2)
#Extend the second list with the sixth list
print("Extend the second list to the sixth one")
time.sleep(2)
d2.extend(d6)
print(d2)
time.sleep(2)
"""
#More on lists
#can access single elements of a list e.g. numbers[0] - first element of the list
# to access the last entry for example would be print(list1[-1])
"""
#Slicing of lists

Things = [0, 'Fred', 2, 'Monkey', 3, 'Uncle Man', "Slime surfacer"]
print(Things)
Things2 = Things[2:5]
print(Things2)

list10 = list(range(16))
print(list10)
list11 = list10[10:14]
print(list11)
"""

"""
#Exercise 12 - Slicing of lists
import random
import time

print("Randomly generating list number 1")
time.sleep(1)
a=random.randint(1,50)
print("lower bound is "+str(a))
time.sleep(1)
b=random.randint(50,100)
print("upper bound is "+str(b))
time.sleep(1)
c=random.randint(1,10)
print("in increments of "+str(c))
time.sleep(1)

d1=list(range(a,b,c))
print(d1)
time.sleep(1)

print("Randomly generating list number 2")
time.sleep(1)
a=random.randint(1,50)
print("lower bound is "+str(a))
time.sleep(1)
b=random.randint(50,100)
print("upper bound is "+str(b))
time.sleep(1)
c=random.randint(1,10)
print("in increments of "+str(c))
time.sleep(1)

d2=list(range(a,b,c))
print(d2)
time.sleep(1)

from os import system
system("clear")

print("Now the lists are created we can look at the slicing")
print()
print("Here is the first randomly generated list we created")
print(d1)
print(lens(d1))
print()
v1 = int(input("How would you like to slice the list: "))
v2 = int(input("How would you like to slice the list: "))
time.sleep(1)
v10 = d1[v1:v2]
print("Here is the original list (d1)")
print(d1)
print("Here is the new list (d1)")
print(v10)
time.sleep(2)
print()
print("Here is our second randomly generated list")
print(d2)
print(lens(d2))
print()
v3 = int(input("How would you like to slice the list: "))
v4 = int(input("How would you like to slice the list: "))
time.sleep(1)
v11 = d2[v3:v4]
print("Here is the original list (d2)")
print(d2)
print("Here is the new list (d2)")
print(v11)

# Special slices
# You can use wildcards for Slicing
# e.g. Numbers [:3] - Generates a sliced list that *contains* the first four entries of the original list
# Numbers[3::] - Generates a sliced list that *starts* at the e.g. fourth entry of the list number
# Numbers[::3] -
"""
#Exercise 13 - Slicing with a:
"""
import random
import time

print("Generating list number 1")
time.sleep(1)

l1length = int(input("How long would you like the list: "))
time.sleep(1)

l1=list(range(l1length))
print(l1)

s1= int(input("First number should be the endpoint of a new list: "))
s2= int(input("Second number should be a starting point of a new list: "))
s3= int(input("Third number should be a skip: "))
s4= int(input("Fourth number should be also be a skip: "))

import random
x=random.randint(1,5) #used as the lower bound for the range
x1=random.randint(1,s1)
x2=random.randint(s2,100)
x3=random.randint(5,100)
x4=random.randint(5,100)

print("List 2")
time.sleep(1)
l2 = list(range(x1,s1)) #x1 is randomly generated, s1 is from the user input etc
print(x1)
print(s1)
time.sleep(1.5)
print(l2)
time.sleep(1)
print()

print("List 3")
time.sleep(1)
l3 = list(range(s2,x2))
print(x2)
print(s2)
time.sleep(1.5)
print(l3)
time.sleep(1)
print()


print("List 4")
time.sleep(1)
l4 = list(range(x,x3,s3))
print(x)
print(x3)
print(s3)
time.sleep(1.5)
print(l4)
time.sleep(1)
print()


print("List 5")
time.sleep(1)
l5 = list(range(x,x4,s4))
print(x)
print(x4)
print(s4)
time.sleep(1.5)
print(l5)
time.sleep(1)
print()
"""
"""
#Shortening lists -
# You can remove entries from lists with the remove command
Mylist = ["apple","banana","orange"]
Mylist.remove("banana")
print(Mylist)
#or
Mylist = ["apple","banana","orange"]
Mylist.remove(Mylist[2])
print(Mylist)
#can also use a range
Mylist = ["apple","banana","orange","pears","grapes"]
del Mylist[2:4]
print(Mylist)
"""
# Exercise 14 - Removing entries.
import time
anotherlist1= ["apple","banana","orange","nuclear winter","grapes"]
anotherlist2= ["football", "100 dead cats", "hockey", "ice skating", "rugby" ]
anotherlist3= ["father", "mother", "brother", "sister", "mutant cannibals"]
print()
print(anotherlist1)
d1= input("Which item doesn't fit in this list?: ")
anotherlist1.remove(str(d1))
print(anotherlist1)
print()
time.sleep(1)
print("Much better ^.^")
time.sleep(1)
print()

print(anotherlist2)
d2= input("Which item doesn't fit in this list?: ")
anotherlist2.remove(str(d2))
print(anotherlist2)
time.sleep(1)
print()
print("Much better ^.^")
print()
time.sleep(1)
print()

print(anotherlist3)
d3= input("Which item doesn't fit in this list?: ")
anotherlist3.remove(str(d3))
print(anotherlist3)
print()
time.sleep(1)
print("Much better ^.^")
time.sleep(1)
print()
