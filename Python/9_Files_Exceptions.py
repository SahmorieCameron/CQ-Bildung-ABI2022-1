#### Writing Files

# To write something into a new file you need the open command in combo with a filename and an operator

# datei=open("neue_datei.txt","w")

# w -stands for write
# a - stands for appending
# r - stands for read

# The first one would overwrite contents included in the file and the second one would add the contents at the end of the file

# After you finish writing, you have to close the files

# datei.close()

# Writing files

# if you wanted to open a file that doesn't exist, it is created.

# You can also work on files with the help of the "with" statment

# By using this statement you don't have to close the files

# with open("bla.txt","w") as with_datei:
#    with_datei.write("Dies ist ein Test \n")

# File = open("Writing python.txt", "w")
# File.write(
#     "This is a test, Hello World\n"
# )  # writing text in file, everything must be a string
# # please not, when adding text, there are no default line breaks. Must add \n.
# File.write("This is a seecond test\n")
# File.close()  # closes the file and saves! V.Important
#
# # if statement
#
# with open("Writing_python.txt", "w") as File_with:
#     for i in range(5):
#         File_with.write("Line " + str(i) + "\n")

#### Exercise 43 - Writing Files
# Write a program that creates two different files.
# The first file should be opened normally and two lines should be written in it.
# Afterwards close the file, open it again and add another three lines of text.

# The second file should be generated by using "with" and a loop to write a coundown from 10 to 0
# Each number should be on a separate line.
# import os
#
# File1 = open("Exercise43_1.txt", "w")
# File1.write(
#     "I said, if you can do it now. It sure would be tough. Now look here come on now. Now make it mellow.\n"
# )
# File1.write("We gonna make it mellow for you now. We gonna make it mellow now.\n")
# File1.close()
#
# File1 = open("Exercise43_1.txt", "a")
# File1.write("You can get it,\n Move to your left, \n Move to your right \n")
#
# with open("Exercise43_2.txt", "w") as File_with:
#     i = 1
#     for i in reversed(range(11)):
#         File_with.write(str(i) + "\n")
#
# # File2 = open("Exercise43_2.txt", "a")
# # File2.write("Liftoff. \n")
# # File2.close()
#
# print("Exercise1")
# os.system("head Exercise43_1.txt")
# print()
# print("Exercise2")
# os.system("head -15 Exercise43_2.txt")

#### Reading files

# There are three variants to read in files
# The first one reads in the whole file at once:
# with open("ein_zu_zehn.txt","r") as lese_datei_
#    inhalt =lese_datei.read()
# print(repr(inhalt))
# The repr() command can show a representation of the contents of the file
# The version above should be used only with smaller files, because the whole contents are put into the memory and you can't work with them.

# The other two options read the file line by line.

# with open("eins_zu_zehn.txt", "r") as lese_datei2:
# zeilen=lese_datei2.readlines()
# print(zeilen)

# In the case above the whole file is read in at once, but each line is a separate entry in the list zeilen

# The last version works with a generator and has the advantage that only one line at a time is read into the memory

# with open("eins_zu_zehn.txt","r") as lese_datei3:
#    for zeile in lese_datei3:
#        print(repr(zeile))

#### Examples

# with open("File.txt","r") as read_file:
#     contents = read_file.read()
# print(contents)
# print(repr(contents))
#
# with open("File.txt", "r") as read_file:
#     contents2=read_file.readlines()
# print(contents2)
#
# with open("Countdown.txt", "r")as read_file:
#     for line in read_file:
#         print(line)

#### Exercise 44 - Reading a File_

# Read in your second file from exercise 39, the one with the countdown, by using the generator method.
# Calculate the sum of the numbers and print out the result.

# with open("Exercise43_2.txt", "r") as read_file:
#     sum = 0
#     for line in read_file:
#         sum += int(line)
# print(sum)
#
# #### Exercise 45 - Copying a file
#
# # Write a program that takes the name of a file from the user and generates a copy of this file.
# # The Copy should be generated by writing the contents of the original file into a new file line by line.
# # Use generators to optimize your memory usage for this exercise.
# import os
#
# # My attempt
# os.system("ls")
# filename1 = input("Please select a file from this directory: ")
# print(f"You have selected {filename1}.")
#
# newfile = []
# with open(filename1, "r") as read_file:
#     for line in read_file:
#         newfile += line
# print(newfile)
#
# File3 = open("Newfile.txt", "w")
# File3.write(str(newfile))
# File3.close()
#
# os.system("head Newfile.txt")
#
# print()
#
# # Here is the optimal method for this exercise.
# File4 = input("Which file do you want to copy: ")
# with open(File4, "r") as read_file:
#     with open(
#         "Copy_" + File4, "w"
#     ) as write_file:  # second file creation, with write permission.
#         for line in read_file:  # Go line through line in the read_file
#             write_file.write(line)  # writes the line to the copy file
#
# os.system("head-20 Copy_Exercise43_2.txt")


#### Raising Exceptions

# Python allows you to raise exceptions, so taht errors occurring during the run of the program don't stop it.

# Consisting of 4 operators

# try: the program tries to run the commands afterwards

# exept: raises exceptions in combination with specific errors

# else: the instructions after this are only run if the try didn't raise an error

# finally: instructions after this is always run, whether errors occurred or not

# i = 0
# while i < 5:
#     try:
#         Number = int(input("Type in a number: "))
#     except ValueError:
#         print("Please type in a number!")
#     except:
#         print("Wrong input")
#     else:
#         print(Number)
#     i += 1

#### Exericse 41 - Exeptions on inputs

# Write a program that runs a simple division
# Generate a random integer and divide it through an integer inputted by the user
# Create an exception for wrong inputs(a string for example)
# Create a second exception to handle division by zero
# Both exceptions should belong to the same try:
# Print out the results of the division a tthe end and try several different inputs

import random

intran = random.randint(0, 101)
try:
    userinput = int(input("Pick a number to be divided: "))
    division = intran / userinput
except ValueError:
    print("No, please pick an actual number")
except ZeroDivisionError:
    print("No, dividing by zero is not allowed")
else:
    print(division)