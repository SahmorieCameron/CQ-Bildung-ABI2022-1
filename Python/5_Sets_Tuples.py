# Python Script for day 5 where we continue learning about dictionaries
# we also continued learning about various other data structures,
# tuples and sets

# # Creating a nested addressbook
# addressbook = {}
# addressbook["blahblah"] = {}
# addressbook["blahblah"]["address"] = ["blahblahtown"]
# addressbook["blahblah"]["Mobile"] = ["0123456789"]
#
# # Exercise 27
#
# book1 = {}
# book1["Harry"] = {}
# book1["Harry"]["Address"] = ["4 Privet Drive, Little Whinging, Surrey"]
# book1["Harry"]["Familiar"] = ["Hedwig"]
# book1["Harry"]["Birthday"] = ["31.07.1980"]
# book1["Harry"]["e-mail"] = ["urawizardarry@aol.com"]
#
# book1["Ron"] = {}
# book1["Ron"]["Address"] = ["15 Ottery St Catchpole, Devon"]
# book1["Ron"]["Familiar"] = ["Scabbers"]
# book1["Ron"]["Birthday"] = ["01.03.1980"]
# book1["Ron"]["e-mail"] = ["kingweasley@gmail.com"]
#
# book1["Hermione"] = {}
# book1["Hermione"]["Address"] = ["1 Mystery House, Somewhere, London"]
# book1["Hermione"]["Familiar"] = ["Cruickshanks"]
# book1["Hermione"]["Birthday"] = ["19.09.1979"]
# book1["Hermione"]["e-mail"] = ["hjgranger@hotmail.co.uk"]
#
# print(book1["Harry"])
# print()
# print(book1["Ron"])
# print()
# print(book1["Hermione"])
#
# # Exercise 19 - Adjusting the addressbook
#
# book2 = {}
# book2["Harry"] = {}
# book2["Harry"]["Address"] = ["4 Privet Drive, Little Whinging, Surrey"]
# book2["Harry"]["Familiar"] = ["Hedwig"]
# book2["Harry"]["Birthday"] = ["31.07.1980"]
# book2["Harry"]["e-mail"] = ["urawizardarry@aol.com"]
# book2["Harry"]["Parents"] = ["..."]
#
# book2["Ron"] = {}
# book2["Ron"]["Address"] = ["15 Ottery St Catchpole, Devon"]
# book2["Ron"]["Familiar"] = ["*Scrambled*"]
# book2["Ron"]["Birthday"] = ["01.03.1980"]
# book2["Ron"]["e-mail"] = ["kingweasley@gmail.com"]
#
# book2["Hermione"] = {}
# book2["Hermione"]["Address"] = ["1 Mystery House, Somewhere, London"]
# book2["Hermione"]["Familiar"] = ["Cruickshanks"]
# book2["Hermione"]["Birthday"] = ["19.09.1979"]
# book2["Hermione"]["e-mail"] = ["hjgranger@hotmail.co.uk"]
#
#
# # Take your dictionary from exercise 27
# # write a program that allows the user to make changes
#
# # Ask the user if he wants to add an entry, delete an entry or change an entry
#
# # If the user wants to delete an entry,
# # ask for the entry which should be removed and remove it
#
# # If the user wants to change an entry ask which part should be changed AND
# # what the content should be
#
# # If the user wants to add an entry,
# # ask for the information necessary to create a new entry
#
# # print the dictionary at the start and end of the program
#
# print(book2["Harry"])
# print()
# print(book2["Ron"])
# print()
# print(book2["Hermione"])
#
# print()
# userinput1 = input(
#     "Would you like to add an new entry, delete an entry or change an entry?: "
# )
# print()
# if userinput1 == "Add" or userinput1 == "add" or userinput1 == "ADD":
#     userinput2 = input("Please add yourself to our addressbook: ")
#     book2[userinput2] = {}
#     userinput3 = input("Please add your address: ")
#     book2[userinput2]["Address"] = [userinput3]
#     userinput4 = input("Please add your animal familiar: ")
#     book2[userinput2]["Familiar"] = [userinput4]
#     userinput5 = input("Please add your birthday: ")
#     book2[userinput2]["Birthday"] = [userinput5]
#     userinput6 = input("Please add your e-mail: ")
#     book2[userinput2]["e-mail"] = [userinput6]
#     print()
#     print(book2)
#     print()
# elif userinput1 == "Delete" or userinput1 == "delete" or userinput1 == "DELETE":
#     userinput7 = input("Would you like to select a person or a key to remove: ")
#     if userinput7 == "person" or userinput7 == "Person" or userinput7 == "PERSON":
#         userinput8 = input("Please select which person to delete: ")
#         del book2[userinput8]
#         print()
#         print(book2)
#     elif userinput7 == "key" or userinput7 == "Key" or userinput7 == "KEY":
#         userinput8 = input(
#             "Please select which person's key to delete from the addressbook: "
#         )
#         print("You have selected " + userinput8 + ".")
#         print(book2[userinput8])
#         userinput9 = input(
#             "Which key to delete from " + userinput8 + " in the addressbook: "
#         )
#         del book2[userinput8][userinput9]
#         print(book2[userinput8])
#         print()
#     else:
#         print("This option is not recognized. Please rerun the programme")
# elif userinput1 == "change" or userinput1 == "Change" or userinput1 == "CHANGE":
#     userinput9 = input(
#         "Please select which person's key to change from the addressbook: "
#     )
#     print("You have selected " + userinput9 + ".")
#     print(book2[userinput9])
#     userinput10 = input(
#         "Which key to update from " + userinput9 + " in the addressbook: "
#     )
#     userinput11 = input("Update the key for " + userinput9 + ".: ")
#     book2[userinput9][userinput10] = userinput11
#     print(book2[userinput9])
# elif userinput1 == "nah" or userinput1 == "no" or userinput1 == "No":
#     print("Then press alt-f4 and go about your business. kmt")
# else:
#     print("This option is not recognized. Please rerun the programme")
#     print()
#     print()


# Here I will put Christoph's code for this exercise as it is slightly different

#### Tuples

# Tuples are another form of datastructures that can be generated in python
# ordered, unchangeable and indexed
# Generated with round brackets
# e.g.
mytuple = ("apple", "banana", "orange")
mytuple = "apple"
# ordered means that you CANNOT change the order of the Values
# you CANNOT add or remove values from the tuple
# can be used as a form of CONSTANT.

# Let's start working with TUPLES

# mytuple1 = (1, 2, 3)
# mytuple2 = (1,)  # must add comma to the end of a tuple with a single entry.
#
# print(mytuple1)
# print(mytuple2)
# print(type(mytuple2))
#
# mytuple3 = ("Hello", "World")
# print(type(mytuple3))
#
# mytuple4 = tuple(range(5))
# print(mytuple4)
# print(type(mytuple4))
# print(mytuple4[1])
# Above are just some examples of tuple creation

#### Exercise 20 - Working with Tuples
# Write a program that creates four tuple of different lengths
# The lengths should be dictated by the user
# Print out the tuples and one user chosen entry from each tuple
# Try to create a tuple that has duplicate values e.g. 1,1,2,2
# import random
#
# mytuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#
# print("We are creating Tuples and we would like you to help")
# print("Here is an example of a tuple " + str(mytuple1) + ".")
# print("Please choose 4 numbers that will represent the length of each tuple")
#
# userinput1 = int(input("Tuple 1: "))
# userinput2 = int(input("Tuple 2: "))
# userinput3 = int(input("Tuple 3: "))
# userinput4 = int(input("Tuple 4: "))
#
# usertuple1 = tuple(range(userinput1))
# usertuple2 = tuple(range(userinput2))
# usertuple3 = tuple(range(userinput3))
# usertuple4 = tuple(range(userinput4))
#
# print("Here are your 4 generated Tuples")
# print()
# print(usertuple1)
# print(type(usertuple1))
# print(usertuple2)
# print(type(usertuple2))
# print(usertuple3)
# print(type(usertuple3))
# print(usertuple4)
# print(type(usertuple4))
# print()
#
# integer = random.randint(1, max(usertuple1))
# print(integer)
# print("Here is a random entry from within your first tuple")
# print(usertuple1[integer])
# print()
#
# print("Please select an entry from each of your Tuples")
# print(usertuple1)
# userselection1 = int(input("Entry from Tuple 1: "))
# print(usertuple2)
# userselection2 = int(input("Entry from Tuple 2: "))
# print(usertuple3)
# userselection3 = int(input("Entry from Tuple 3: "))
# print(usertuple4)
# userselection4 = int(input("Entry from Tuple 4: "))
#
# print(usertuple1[userselection1])
# print(usertuple2[userselection2])
# print(usertuple3[userselection3])
# print(usertuple4[userselection4])
#
# # Trying a tuple with duplicates... seems to work...
# duplicatetuple = (1, 1, 1, 4, 4, 2, 9, 8, 9)
# print(duplicatetuple)
# print(type(duplicatetuple))

#### Sets

# Sets are the last type of data structure that is included in standard python.
# Sets are unordered, unchangeble and can't be indexed.
# They are also created with curly brackets {} but you can't create empty steps.

# myset = {"apple", "banana", "orange"}
# print(myset)
# print(type(myset))
# myset = {"apple"}
#
# # The order of the values can change on different calls (unordered)
# # Cannot change the items in the set but you can add or remove entries
#
# myset2 = {1, 2, 3, 4, 4}
# print(myset2)

# printing sets with duplicates doesn't print the duplicates
# can use this to print LISTS with only unique entries

list1 = [1, 2, 3, 4, 4, 4, 4, 4, 5, 6]
print(list1)
list2 = list(set(list1))
print(list2)

# can also cast sets using range operator

myset3 = set(range(5))
print(myset3)

# Exercise 21 - Working with sets

# Create four sets of different lengths
# The lengths should be dictated by the user
# Print out the sets
# Try to add duplicate values to the sets

myset1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print("We are creating sets and we would like you to help")
print("Here is an example of a set " + str(myset1) + ".")
print("Please choose 4 numbers that will represent the length of each set")

userinput1 = int(input("Set 1: "))
userinput2 = int(input("Set 2: "))
userinput3 = int(input("Set 3: "))
userinput4 = int(input("Set 4: "))

userset1 = set(range(userinput1))
userset2 = set(range(userinput2))
userset3 = set(range(userinput3))
userset4 = set(range(userinput4))

print("Here are your 4 generated Sets")
print()
print(userset1)
print(type(userset1))
print(userset2)
print(type(userset2))
print(userset3)
print(type(userset3))
print(userset4)
print(type(userset4))
print()

# Elements of sets

# You can remove elements of sets to be able to work with them with the help of the pop command
# You can only remove 1 entry at a time
# the command below would remove the 1st entry of our set and assign to variable elem.
# elem = userset1.pop()
# elem2 = userset1.remove(#item that you want to remove)
# print(userset1)
# print(elem)
# print(elem2)
# Adding to a set

# userset1.add(19)  # puts the value at the end of the set

# Exercise 22 - Adding and removing
# using the sets from exercise 21, remove some elements from them
# Try to remove two elements directly one after the other
# check which elements were removed with the print command
# add the elements again to the set
# print out the new sets
# what changes can you see
print("Exercise22")
pop1 = userset1.pop()
pop2 = userset1.pop()
print(pop1)
print(pop2)
print()
print(userset1)
print()
userset1.add(pop1)
userset1.add(pop2)
print()
print(userset1)
print()

#### Summary - datastructures

# YOu should know the basics of the four basic datastructures included
# in the standard python package

# list
# dictionary
# tuple
# set

# made up of different elements, strings, integers, floats etc.
