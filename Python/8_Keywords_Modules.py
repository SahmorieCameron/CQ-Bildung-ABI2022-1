#### Keywords

# In Python there are 3 keywords you should know:

# break

# continue

# pass

# Each of them has different uses which we will discuss...

# try to use them only if they are really necessary!

#### Break

# Break stops a loop, you can use it if you are searching for something and don't need to run over the rest of the loop.

# Mainly used to reduce the running time of programs if you are only interested in certain parts of the calculation.

#### Continue

# Continue can be used to skip parts of a loop.

# All commands that follow a continue in a loop aren't executed.

# You can use this if you don't want your program to go over multiple if statements or other loops nested inside your loop.

# Use it only if you can be sure that you don't need the remaining calculations in the current iteration.

# # e.g.
# import random
#
# list1 = random.sample(range(10, 100), random.randint(5, 10))
# print(list1)
# # BREAK
# sum2 = 0
# for i in range(len(list1)):
#     sum2 += list1[i]
#     if sum2 > 100:
#         break
# print(sum2)
# # CONTINUE
# sum3 = 0
# for i in range(len(list1)):
#     sum3 += list1[i]
#     if sum3 > 100:
#         continue
#     print(i)
# print(sum3)

#### Pass

# Pass can be used as a placeholder for future code.

# In python, empty code is not allowed in function definitions, loop, if statements or class definitions.

# You should use this only in combination with comments that tell what you want to do in this place later on.

# Used often when constructing programs.
# used to test out code and create structure

#### Exercise 64 - Keywords in python

# Create a list with at least 15 random entries
# Iterate over it with a FOR loop and add up the elements
# Create one IF statement in your loop that can't be true and add a PASS
# Include a second IF statement in you loop that breaks the loop if your sum gets bigger than a threshold (your choice)
# Include a third IF statement in your loop that uses continue if the current entry of your list is in a specific range, e.g. 50 to 60, and prints out something in all other cases (use else)
# Print out the sum and the number iterations run

# import random
#
# list1 = random.sample(range(1, 50), 15)
# print(list1)
# # BREAK
# sum2 = 0
# for i in range(len(list1)):
#     sum2 += list1[i]
#     print(i)
#     if sum2 == "Dog":
#         pass
#     elif sum2 > 200:
#         break
#     if sum2 < 100 and sum2 > 50:
#         print("DANGERZONE")
#     else:
#         print("SAFE")
# print("The final sum is " + str(sum2))

#### Using modules

# You can use more functions by using additional modules in python

# With the help of the IMPORT operator you can read in external Functions

# Note that programs should NOT have the same name as modules, e.g. calendar, since the operator import would look for a file called calendar.py for example. The program would try to read in itself....

# Finding commands for standard modules

# To see which commands are available for standard modules, either look in the library reference (if you downloaded it) or go to https://docs.python.org/3/library/

# For the module calendar you can find the function prcal that prints a calendar for a year

# To use this function you need the call calendar.prcal(year)
# if you don't want to use all functions you can use:
# From calendar import prcal
# From time import time, ctime

# import calendar
#
# Year1 = calendar.prcal(2022)
# print(Year1)
#
# from calendar import prcal
#
# Year2 = prcal(2020)
# print(Year2)

# Exercise 33 - New modules

# Write a program that asks the user to guess a specific number
# Generate a random number between 0 and 99, search the library to find a module and a function for this task
# Generate a while loop that asks for a guess as long as the user didn't guess right
# Print out hints if the user is lower or higher than the random number
# Count the number of guesses the user needed and print them out after the user guessed correctly
#
# import random
#
# i = 1
# Number = random.randint(1, 100)
# Guess1 = 0
# while int(Guess1) != Number:
#     print("Try " + str(i))
#     Guess1 = input("Guess a number ")
#     if int(Guess1) == Number:
#         print("Great! I was thinking of " + str(Number))
#         print("To guess my number it took you " + str(i) + " guesses")
#         if i >= 10:
#             print("Hmm, not great. I think you can do better")
#         else:
#             print("Wow, are you psychic?")
#             break
#     elif Number < int(Guess1):
#         print("Lower")
#     elif Number > int(Guess1):
#         print("Higher")
#     i += 1
#     print()

#### os

# Provides a portable way of using operating system dependent functionality

# Simply put, you can use Linux/Bash commands in your python placeholder

# Some functions have names analogous to bash commands
# e.g. os.chdir(path) - change directory, analogous to cd
# os.getcwd() - get a string representing the current directory
# os.mkdir(path) - create a new directory
# os.rename(src, dst) -rename file or directory src to dst
# os.system("command") - Run the given command in a subshell, you can use Linux commands as Strings to run from your program.

#### Exercise 34 - Working with os

# Create a directory structure using os
# Create one parent directory with at least 5 child directories
# Create a file in each directory simply by using os and by changing directories beforehand
# import sys, os
#
# os.system("cd $HOME")
# os.mkdir("Ex34.dir")
# os.system("cd $HOME/Ex34.dir")
# os.system("ls")
# i = 0
# for i in range(5):
#     os.system("cd $HOME/Ex34.dir")
#     os.system("ls")
#     os.mkdir("DIR_" + str(i))
#     os.system("cd $HOME/Ex34.dir/DIR_" + str(i))
#     os.system("touch file" + str(i) + ".txt")
# os.system("ls")

#### math

# Provides access to mathematical functions and constants

# Cannot be used with complex numbers
# use cmath instead

# The distinction between funtions that can use complex numbers and those which don't is made since most user don't want to learn so much maths.

# All returned values are floats.

# Examples math

# math.isnan(x) - Returns true if x is not a number

# math.exp(x) - returns e raised to the power x

# math.log(x[,base]) - With one argument returns the natural logarithm (to base e)
#                    - with two arguments returns the logarithm of the given base

# math.pow(x,y) - Returns x to the power y
# math.sqrt(x) - returns the square root of x

# etc etc

#### Exercise 35

# Write a program that takes two numbers (x and y) from the user and calculates new values with the help of the math functions on the previous slides (exp, log, log2, log10, pow, sqrt, cos, sin, tan, acos, asin, atan)
# Print the results

x = int(input("Pick a number: "))
y = int(input("Pick a second number: "))

import math

exp = math.exp(x)
logy = math.log(x)
logy2 = math.log2(x)
logy10 = math.log10(x)
powa = math.pow(x, y)
sqrrt = math.sqrt(x)
cosine = math.cos(x)
sine = math.sin(x)
tangent = math.tan(x)
print(
    str(exp)
    + str(logy)
    + str(logy2)
    + str(logy10)
    + str(powa)
    + str(sqrrt)
    + str(cosine)
    + str(sine)
    + str(tangent)
)
