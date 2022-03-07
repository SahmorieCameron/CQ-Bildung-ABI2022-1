"""
This is the script of our third day working with Python
We finished out lessons about if statements and than started working on
data structures like lists. We covered the creation of lists, the operators
len() and range(), how to slice lists and last but not least we worked on
multi-dimensional lists. Keep in mind that this is no real program but a
collection of commands with comments for your study afterwards.
"""
# We will create a simple list containing the week days
# weekdays = [
weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
# We can print out this list
print(weekdays)

MonList = ["Vegetables", "Fruit", "Bread", "Eggs"]
print(MonList)
WedList = ["Bread", "Eggs", "Mozarella", "Canned Tomatoes", "Yeast", "Flour"]
print(MonList)
FriList = ["Vegetables", "Eggs", "Bread", "Toilet Paper"]
print(FriList)

# We can access specific entries in a list with [] and the index, remember in
# Python the indexing starts with 0
print("The second entry in the list weekdays is " + weekdays[2])
# To access a position with the help of a user input you would have first
# create a variable with the user input, called Pos here
Pos = int(input("Which position: "))
# Than you could access the entry in the list with a variable, but the variable
# has to be of the type int
print("The entry on position " + str(Pos) + " in the list weekdays is " + weekdays[Pos])
# You can always create lists that combine values of different types
Example = [1, 3, "Hello", "World", 1.56]
print(Example)
print("The list above contains on Positions 0, 2 and 4 the following data types")
print(type(Example[0]))
print(type(Example[2]))
print(type(Example[4]))

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

# Python can create lists that include integers and strings
Horses = [1, "Gerry Klaferty", "Off to the races", 2]
print(Horses)

# Here is the code how access a specific position in a list
Pos = int(input("Which position"))
print(weekdays[Pos])
"""
"""
# Can also use the range funtion to generate lists
Numbers = list(range(16))
print(Numbers)
#
Numbers2 = list(range(5, 26))
print(Numbers2)
# ^creates and prints a list ranging from 5 to 26
Numbers3 = list(range(0, 21, 2))
print(Numbers3)
# ^creates and prints a range between 0 and 21, but only in increments of 2
# You can check for the lengths of lists with the help of the len() function
C = len(Numbers)
print(C)

# We can elongate lists witht he help of two commands called append and extend
# Both operations are done in place, that means you change the value of the list
# you elongate with these commands. So you have to keep in mind that the list
# that is returned differs from the list you used for this operation
# We start by generating three lists for this example
list1 = list(range(4))
list2 = list(range(4))
list3 = list(range(4))
print("The example lists list1, list2 and list3 look like this:")
print(list1)
print(list2)
print(list3)
# Now we append the third list to the first list and create a multi-dimensional
# list. Append adds the list3 as a whole to list1 so that list3 is now on index
# 4 of the first list
list1.append(list3)
print("list1 looks now like this:")
print(list1)  # We print out the whole new list
# We print out the length of the new list
print("The lenght of list1 is " + str(len(list1)))
print("The index 4 (fifth entry) of list1 looks like this:")
print(list1[4])  # We print out the entry on index 4 of the new list
# If you want to access a specific entry in the added list you have to use
# two indices
print("The third entry of the list contained in list1 looks like this:")
print(list1[4][2])
# Normally append is used with single values since it doesn't iterate of the
# contents given to it
list1.append(5)
print(list1)
# If we use extend, the entries of the list we want to add to our old list
# are added to it element-wise. The operator extend iterates over the contents
# of list2 in the example below and adds its values to the list3
list3.extend(list2)
print(list3)  # We print out the whole new list
# We print out the length of the new list
print("The lenght of list3 is " + str(len(list3)))
print(list3[4])  # We print out the entry on index 4 of the new list
# If we use extend with a string the list would be extended with   each letter of the string as a new entry of the list
list3.extend("Hello")
print(list3)
# We can also use the "+" to combine two lists, but this doesn't work in place
# so you have to define a new variable list5 like in the example below. This can
# be used if you don't want to change your previously defined lists
list4 = list(range(6))
# We print out our two lists
print("Our test lists look like this")
print(list2)
print(list4)
# Now we combine our lists and create the new list list5
list5 = list2 + list4
# Now we print out all three lists again
print("The two example lists and the added list look like this:")
print(list2)
print(list4)
print(list5)
# You can access the last entries of a list by using negative indices
# The first example below accesses the last element of list5
print(list5[-1])
# In this example we access the second to last element of list1 (the added list) and than access the second element of this added list
print(list1[-2][2])

r1 = list(range(0, 50))
print("1: 0,50")
r2 = list(range(0, 100))
print("2: 0,100")
r3 = list(range(0, 150))
print("3: 0,150")
r4 = list(range(0, 200))
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

# We now want to work on slices of lists, therefore we generate a new, longer
# list at first
list6 = list(range(16))
# Now we print out the whole list first
print("list6 looks like this:")
print(list6)
# Now we print out only a part of the list by using a slice. The printed out
# lists includes the value on index2 of list6 but excludes the value on index
# 9 of list6
print("Indices 2 until 8 of list6 look like this:")
print(list6[2:9])
# We can even use slices to hand over only parts of a list to a new variable
# in this case the list7 contains the values of the indices 10, 11 ,12 and 13
# because the value of index 14 was excluded
list7 = list6[10:14]
print("The new list containing Indices 10 to 13 of list6 looks like this:")
print(list7)

# We can use some kind of wildcards for slices by using ":"
# With the list6 above we could use the example below to get all values from
# the fourth entry until the end
print("The entries of list6 starting at Index 3 look like this:")
print(list6[3:])
# To access all entries until the third one we could use a print like this:
print("The first three entries of list6 look like this:")
print(list6[:3])
# If we use two ":" before a number in the slice only each third number would
# be returned:
print("Using :: we would get a list like this:")
print(list6[::3])
# Last but not least we can use ::-1 to reverse a list
print("Reverse of list6:")
print(list6[::-1])

# We now want to shorten lists by removing certain elements from them
# Please note that every time you remove something from a list the indices are adjusted accordingly. So if you remove the third entry,the entry on index 4 in the original list is now on index 3 in the adjusted list. All operations below are done in place, that means you change the contents of your variable and don't create new ones
mylist = ["apple", "banana", "orange", "apple", "lemon", "melon", "peach"]
print(mylist)
# We can remove specific entries just by handing over the value we want to remove
mylist.remove("lemon")
print(mylist)
# We can also remove entries by using indices if we don't know the exact value
mylist.remove(mylist[2])
print(mylist)
# If we have duplicates in our list, remove() only removes the first occurence
# of this value and leaves the remaining intact
mylist.remove("apple")
print(mylist)
# With the help of slices and the del command we can remove several entries at
# once
del mylist[1:3]
print(mylist)


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
time.sleep(1)
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
# More on lists
# can access single elements of a list e.g. numbers[0] - first element of the list
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
# Exercise 13 - Slicing with a:
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
"""
# Exercise 14 - Removing entries.
import time

anotherlist1 = ["apple", "banana", "orange", "nuclear winter", "grapes"]
anotherlist2 = ["football", "100 dead cats", "hockey", "ice skating", "rugby"]
anotherlist3 = ["father", "mother", "brother", "sister", "mutant cannibals"]
print()
print(anotherlist1)
d1 = input("Which item doesn't fit in this list?: ")
anotherlist1.remove(str(d1))
print(anotherlist1)
print()
time.sleep(1)
print("Much better ^.^")
time.sleep(1)
print()

print(anotherlist2)
d2 = input("Which item doesn't fit in this list?: ")
anotherlist2.remove(str(d2))
print(anotherlist2)
time.sleep(1)
print()
print("Much better ^.^")
print()
time.sleep(1)
print()

print(anotherlist3)
d3 = input("Which item doesn't fit in this list?: ")
anotherlist3.remove(str(d3))
print(anotherlist3)
print()
time.sleep(1)
print("Much better ^.^")print(x)

time.sleep(1)
print()

"""

"""
### Checking for values in lists using check function

Mylist = [0, 1, 2, 3, 4, 5, 6]
Check1 = 4
Check2 = 12
if Check1 in Mylist:
    print("This value is in the list")
if Check2 not in Mylist:
    print("This value is not in the list")

# Exercise 61 - Checking for values

import random

print("I have created a random list, try to guess 3 numbers within the list")
x = random.randint(1, 50)
y = random.randint(10, 300)
z = list(range(x, y))
print()
print()

number1 = int(input("Guess another number in the list: "))
Check1 = number1
if Check1 in z:
    print(str(Check1) + " is within this range. Great guess!")
else:
    print(str(Check1) + " is not present within this range. Bad guess!")

number2 = int(input("Guess another number in the list: "))
Check2 = number2
if Check2 in z:
    print(str(Check2) + " is within this range. Great guess!")
else:
    print(str(Check2) + " is not present within this range. Bad guess!")

number3 = int(input("Guess another number in the list: "))
Check3 = number3
if Check3 in z:
    print(str(Check3) + " is within this range. Great guess!")
else:
    print(str(Check3) + " is not present within this range. Bad guess!")
"""
"""Inserting values - you can insert values at a specific point in a list
with the help of the insert command"""
"""
Mylist3 = list(range(1, 11))
print(Mylist3)
Mylist3.insert(5, 100)
print(Mylist3)
Mylist3[10] = "Drama"
print(Mylist3)
Mylist3[10] = "10"
print(Mylist3)
del Mylist3[5]
print(Mylist3)
"""
"""
# Exercise 62 - Inserting values
# Generate three lists of different sizes and print them out
# Let the user choose where on these lists they want to insert which number
# Don't forget to check whether the chosen index is part of the list or not.

import random

x1 = random.randint(1, 300)
x2 = random.randint(1, 100)
x3 = random.randint(1, 150)
y1 = list(range(x1))
print(min(y1))
print(max(y1))
y2 = list(range(x2))
y3 = list(range(x3))

print("Here is a list between " + str(min(y1)) + " and " + str(max(y1)) + ".")
userinput1 = str(input("Add a random word to the first list: "))
pos1 = int(input("Select a position to add the word: "))
y1.insert(pos1, userinput1)
print(y1)
Check1 = userinput1
if Check1 in y1:
    print(str(Check1) + " has been added. Well Done!")
else:
    print(str(Check1) + " has not been added. You have failed!")
print()

print("Here is another list between " + str(min(y2)) + " and " + str(max(y2)) + ".")
userinput2 = str(input("Add a random word to the list: "))
pos2 = int(input("Select a position to add the word: "))
y2.insert(pos2, userinput2)
print(y2)
Check2 = userinput2
if Check2 in y2:
    print(str(Check2) + " has been added. Well Done!")
else:
    print(str(Check2) + " has not been added. You have failed!")
print()

print("The last list between " + str(min(y3)) + " and " + str(max(y3)) + ".")
serinput3 = str(input("Add a random word to the last list: "))
pos3 = int(input("Select a position in the list to add the word: "))
y3.insert(pos3, userinput3)
print(y3)
Check3 = userinput3
if Check3 in y3:
    print(str(Check3) + " has been added. Well Done!")
else:
    print(str(Check3) + " has not been added. You have failed!")
"""
# Other list functions!
#
# sort() - sort the list in ascending order.
# index() - returns the first appearance of a particular value.
# max(list) - returns the maximum value.
# min(list) - returns the minimum value.
# clear() - removes all entries from the list.
# count() - returns the number of elements with the required value. Counts specific items in lists
# reverse() - reverses the order of the list.
# copy() - creates a duplicate of the list.

# all () functions above e.g. sort() must be used like mylist.sort()

# Multidimensional lists!!

# Contain two or more running indices
# Are the least standardized

# [[],[]] - is a possible listing for 2D lists ! Especially important for matrices

# A matrix is a 2D vectors with 2 indices

# M X N is a matrix with the dimensions N and M

# Operations on the matrix are part of the linear algebra

# E.g.
# matrix1 = [list(range(5))] * 5
#
# # Or
#
# matrix2 = [[0, 1, 2], [0, 1, 5], [0, 1, 2]]
# print(matrix1)
# print()
# print(matrix2)
# print()
# print(matrix1[1][2])
# print()
# Exercise 15 - New matrices

# Write a program that creates at least three different matrices with different sizes
# One of them should be quadratic
# One should have more columns than rows
# One should have more rows than columns
# Let the user input the dimensions of your matrices
"""
# Quadratic
M1 = [list(range(6))] * 6
print(M1)
# More columns than rows
# M2 = [list(range(COLUMNS))] * ROWS
M2 = [list(range(10))] * 4
print(M2)
# More rows than columns
M3 = [list(range(4))] * 10
print(M3)
# Let the user input the dimensions of your matrices
userinput1 = int(input("Choose the first dimension of your own matrix: "))
userinput2 = int(input("Choose the second dimension of your own matrix: "))

M4 = [list(range(userinput1))] * userinput2
print(M4)
"""
# Removing entries
# if you want to remove entries from a multi-dimensional list
# you have to use remove in a slightly different way
#
# List1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# List2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# List3 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
#
# # List[selects the sublist within our list].remove(selected_sublist[column][row])
# # value from the (List1[0][0] removed from List1[0])
# # e.g. List1[Column][Row] = "value"
# # List1[0][0] = 1
# # function therefore removes value "1" from the List1[sublist]
#
#
# List1[0].remove(List1[0][0])
# print(List1)
# List2[1].remove(List2[0][0])
# print(List2)
# List3[2].remove(List3[0][0])
# print(List3)
# List1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# List2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# List3 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# print()
# List1[0].remove(List1[1][0])
# print(List1)
# List2[1].remove(List2[1][0])
# print(List2)
# List3[2].remove(List3[1][0])
# print(List3)
# print()
# List1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# List2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# List3 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# List1[0].remove(List1[1][1])
# print(List1)
# List2[1].remove(List2[1][1])
# print(List2)
# List3[2].remove(List3[1][1])
# print(List3)
# print()

# Dictonaries
# Dictionaries have keys and values
# The keys are used to find the corresponding values and are strings
# The line numbers = {} tells python that the variable numbers is a dictionary
# The command numbers.key() returns...
#
# Numbers = {}  # Generates empty dictionary.
# # Curly brackets can only be used during the initiation of the dictionary
# # e.g. can also perfom the initiation as Numbers = {"Sahmorie": 124}
# # Define a new key and add some values
# Numbers["Sahmorie"] = 124
# Numbers["Cameron"] = 500
# Numbers["Jusu"] = 9
# print(Numbers)
# # List of keys in dictionary
# print(Numbers.keys())
# # Access the value for specific keys
# print(Numbers["Jusu"])
# # All the values of all the keys
# print(Numbers.values())
# # Can also use if functions
# if "Cameron" in Numbers:
#     print("Cameron is known")
# #Removing a entry
# del Numbers["Jusu"]

# Exercise 16 - Simple Dictionary

# import time
#
# Dictionary = {}
# Dictionary["a"] = 1
# Dictionary["b"] = 2
# Dictionary["c"] = 3
#
# print(Dictionary)
#
# print("Please continue this trend")
# userinputletter1 = input("What would the next letter of this trend be?: ")
# userinputnumber1 = int(input("And what value would this letter have?: "))
#
# Dictionary[userinputletter1] = userinputnumber1
# print(Dictionary)
#
# Dictionary["h"] = 12
# time.sleep(1)
# print()
# print("Someone has added the next letter and number to our trend")
# print(Dictionary)
# print()
# userinput = input("Does this appear correct?: ")
# if userinput == "No" or "no" or "NO":
#     time.sleep(1)
#     print("Then we will remove it and try again")
#     del Dictionary["h"]
# else:
#     print("Hmm..")
# time.sleep(1)
# print()
# print(Dictionary)
# time.sleep(1)
# userinputletter2 = input("What would the correct next letter of this trend be?: ")
# userinputnumber2 = int(input("And what value would this letter have?: "))
# time.sleep(1)
# Dictionary[userinputletter2] = userinputnumber2
# print(Dictionary)
#
# if userinputletter2 == "e" and userinputnumber2 == 5:
#     time.sleep(1)
#     print("Congratulations")
# else:
#     print("Hmm..")

# Exercise 17 - Searching in dictionaries

NewDictionary = {}
NewDictionary["Nostalgia"] = 1
NewDictionary["Sentimentality"] = 2
NewDictionary["Longing"] = 3
NewDictionary["Yearning"] = 4
NewDictionary["Romanticism"] = 5
NewDictionary["Saudade"] = 6
NewDictionary["Wanderlust"] = 7
NewDictionary["Wistful"] = 8
NewDictionary["Angst"] = 9
NewDictionary["Melancholy"] = 10

ModDict = NewDictionary.copy()  # Copies our Dictionary (we will alter the new one)

UP1 = input(
    "We are collecting synonym of the word 'nostalgia'. Please think of a new one?: "
)
if UP1 in NewDictionary:
    print("Your selection is already known")
else:
    print("Great. That one is new! Let's add it to our list!")

ModDict[UP1] = 11
print(ModDict)

UP2 = input(
    "We are collecting synonym of the word 'nostalgia'. Please think of a new one?: "
)
if UP2 in ModDict:
    print("Your selection is already known")
else:
    print("Great. That one is new! Let's add it to our list!")

ModDict[UP2] = 12
print(ModDict)

UP3 = input(
    "We are collecting synonym of the word 'nostalgia'. Please think of a new one?: "
)
if UP3 in ModDict:
    print("Your selection is already known")
else:
    print("Great. That one is new! Let's add it to our list!")

ModDict[UP3] = 13
print()
print("Here is our old dictionary without your help")
print(NewDictionary)
print()
print("And our new dictionary without your help :)")
print(ModDict)

# Recap!!!
# Dictionaries have keys and values
# Keys can be strings or numbers
# Keys point to values
# Values can be any type of variable, including lists or dictionaries,
# that can also contain lists or dictionaries and so on. We will continue with
# on day 5.
