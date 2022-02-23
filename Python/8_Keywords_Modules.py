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
#
# x = int(input("Pick a number: "))
# y = int(input("Pick a second number: "))
#
# import math
#
# exp = math.exp(x)
# logy = math.log(x)
# logy2 = math.log2(x)
# logy10 = math.log10(x)
# powa = math.pow(x, y)
# sqrrt = math.sqrt(x)
# cosine = math.cos(x)
# sine = math.sin(x)
# tangent = math.tan(x)
# accos = math.acos(x)
# print(
#     str(exp)
#     + str(logy)
#     + str(logy2)
#     + str(logy10)
#     + str(powa)
#     + str(sqrrt)
#     + print()
#     + str(cosine)
#     + print()
#     + str(sine)
#     + print()
#     + str(tangent)
#     + print()
#     + str(accos)
# )

#### Exercise 36 - Working with constants
# math.pi, math.e, math.tau
# Write a second program that takes again two numbers from the user and calculates new values with the pi,e and tau functions.
# This time the input variables have to multiplied by one of three shown constants (Pi, Euler number or Tau)
# Let the user choose which constant should be used.
# Print the results
# import math
#
# userinput1 = int(input("Please select a number: "))
# userinput2 = int(input("Please select a second number: "))
#
# userinput3 = input("Which constant should we use, pi, euler or tau?: ")
# if userinput3 == "pi":
#     print(math.pi * userinput1)
# elif userinput3 == "euler":
#     print(math.e * userinput1)
# elif userinput3 == "tau":
#     print(math.tau * userinput1)
# else:
#     print("Your selection is not acceptable, please try again.")

#### random

# as you should already know, this module implements pseudo-random number generators

# e.g. random.randint(a,b)

# Other methods are:

# random.random() > random number between 0 and 1
# random.gauss(mu,sigma) > normal distribution
# random.shuffle(x) > mixes list randomly

#### Exercise 37 - Random Generator

# Write a program that generates several random numbers
# Let the user input the range for three random integers
# Let the user choose how many random floats between 0 and 1 should be created
# Let the user put in at least two mu and two sigma to create normal distribution values
# What happens if you switch these two values
# Last but not least put all generated values into a list, print the list, shuffle and print again.
#
# import random
#
# userinput1 = int(
#     input("Select the range from which we will generate 3 random numbers: ")
# )
# userinput2 = int(
#     input("Select the range from which we will generate 3 random numbers: ")
# )
# userinput3 = int(
#     input("Select the range from which we will generate 3 random numbers: ")
# )
# userinput4 = int(
#     input("Select the range from which we will generate 3 random numbers: ")
# )
# userinput5 = int(
#     input("Select the range from which we will generate 3 random numbers: ")
# )
# userinput6 = int(
#     input("Select the range from which we will generate 3 random numbers: ")
# )
#
# random1 = random.randint(userinput1, userinput2)
# random2 = random.randint(userinput3, userinput4)
# random3 = random.randint(userinput5, userinput6)
#
# print("Here are our three randomly generated number ", random1, random2, random3)
# print()
# print("Now we can create some random floats!")
# userfloats = int(
#     input("How many random floats between 0 and 1 would you like to create: ")
# )
# floatlist = []
# for i in range(userfloats):
#     floatlist.append(random.random())
# print(floatlist)
#
#
# usermew = int(input("Mu values: "))
# usermewtwo = int(input("Mu values: "))
# usersigma = int(input("Sigma values: "))
# usersigma2 = int(input("Sigma values: "))
#
# print(
#     "With our mu and sigma values, we can create normal distributes e.g.",
#     random.gauss(usermew, usersigma),
# )
# print("And again", random.gauss(usermewtwo, usersigma2))
#
# print(
#     "If we switch the mu and sigma values, our normal distribution changes",
#     random.gauss(usersigma, usermew),
# )
# print("Here too", random.gauss(usersigma2, usermewtwo))
#
# superlist = [
#     userinput1,
#     userinput2,
#     userinput3,
#     userinput4,
#     userinput5,
#     userinput6,
#     usermew,
#     usermewtwo,
#     usersigma,
#     usersigma2,
# ]
# superlist.extend(floatlist)
# print("Here is our superlist", superlist)
# random.shuffle(superlist)
# print("Here is our shuffled superlist", superlist)

#### NumPy

# The fundamental package for scientific computing in python
# At the core is the ndarray object
# NumPy arrays have a fixed size at creation
# The elements in a NumPy array are all required to be of the same data type
# NumPy arrays facilitate advance mathematical and other types of operations on large numbers of data
# import numpy as np > convention for the import of the numpy module.

# Examples NumPy

# Arrays in numpy can be created in various ways.

# np.array([4,3,2,1])>[4,3,2,1]
# np.arange(4)>[0,1,2,3]
# np.zeros(4)>[0,0,0,0]
# np.ones(4)>[1,1,1,1]
# np.zeros((3,4,))>[[0,0,0,0],[0,0,0,0][0,0,0,0]]
# np.arange(15).reshape(3,5)> [[0,1,2,3,4,],[5,6,7,8,9],[10,11,12,13,14]]
# np.random.randn(6,4)

# Basics NumPy
# All operations on arrays apply elementwise
# [1,2,3]*3 > [3,6,9]
# [10,20,30,40]-[0,1,2,3]>[10,19,28,37]

# There are basic functions like:
# arrayname.sum()
# arrayname.min()
# arrayname.max()
# arrayname.transpose() - flips number of rows and number of coloums
# arrayname.shape - tells you the dimensions of your current array

# import numpy as np
#
# #
# # Array1 = np.array([5, 6, 8, 1, 5])
# # Array2 = np.ones(5)
# # Array3 = np.zeroes((3, 6))
# # Array4 = np.ones(((5, 6, 7)))
# # Array5 = np.arange(16).reshape(3, 5)
# # Array6 = Array1.sum()
# # Max1 = Array1.max()
# # Min1 = Array1.min()
# # print(Array1.shape)
# # print(Array6.shape)
# # print(Array6.max())
# # print(Array1.transpose())
# # matrix,row, column
#
# #### Exercise 38 - NumPy arrays
#
# # Write a simple python program that generates the following arrays:
# import numpy as np
#
# # An array consisting of 25 zeroes
# print("An array consisting of 25 zeroes\n", np.zeros(25))
# print()
# # An array consisting of 8 ones
# print("Here is an array consisting of 8 ones\n", np.ones(8))
# print()
# # An array consisting of numbers from 0 to 25 in order
# print(
#     "Here is an array consisting of numbers from 0 to 25 in order\n",
#     np.array(range(25)),
# )
# print()
# # An array consisting of 9 entries of your choice
# yeah = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
# print("An array with 9 entries of my choice\n", yeah)
# print()
# # A two-dimensional array TD consisting of 6 rows of arrays with 5 entries
# TD = np.random.randn(6, 5)
# print("2D array, 6 rows and 5 entries\n", TD)
# print()
# # A transposed version of the two-dimensional array TD
# print("2D array transposed\n", TD.transpose())
# print()
# # Write an algorithm to print out the sum, maximum and min value + the shape of all created arrays.
# def algorithm(array):
#     print("Array sum\n", (array).sum())
#     print("Array max\n", (array).max())
#     print("Array min\n", (array).min())
#     print("Array shape\n", (array).shape)
#
#
# print(algorithm(yeah))

#### Scipy

# SciPy is a collection of mathematical algorithms and convenience functions build on the NumPy extension of python

# With SciPy, an interactive Python session becomes a data-processing and system-prototyping environment rivaling systems, such as MATLAB etc.

# SciPy sub-packages need to be imported separately
# from scipy import linalg, optimize

#### Pandas

# When working with tabular data, such as data stored in spreadsheets or databases, pandas is the right tool for you.
# In pandaas, a data table is called a DataFrame
# pandas supposrts the integration with many file formats or data sources out of the box
# csv, excel, sql, json, parquet
# There is no need to loop over all rows of your data table to do calculations.
# Data manipulations on a column work elementwise
# Adding a column to a DataFrame based on existing data in other columns is straightforward.

# Syntax Pandas

# Standard import:import pandas as pd
# two data types: Series and DataFrames
# Series = 1D
# DataFrame = 2D - Column name, row name
# some essential functions incl:
# df.sum
# df.describe()
# df.sort_index(axis=1,ascending=False)
# df.sort_value(by="B")
# df.index or df.columns

# difference between lists and pandas series...?

# import pandas as pd
# import numpy as np

# dataframe1 = pd.DataFrame(
#     np.random.randn(2, 4), index=["Test1", "Test2"], columns=list("ABCD")
# )
# print(dataframe1)
#
# # accessing specific values in dataframe
# # indexname or column name
#
# print(
#     dataframe1.loc["Test1", "C"]
# )  # .loc can access specific values using the index name and the column name
#
# # second way
# # using numbers - iloc
#
# print(
#     dataframe1.iloc[0][1]
# )  # first number = row, second number = column # in this example first row second column
#
# # adding data to dataframe
#
# dataframe1.loc["Test3", "B"] = 2.46  # creates a new row with the value after the =
# print(dataframe1)
#
# # there are other functions e.g. sum , results are columnwise
#
# print(dataframe1.sum())
# print(dataframe1.sum(axis=1))
# print(dataframe1.index)  # used to iterate over indices
# for Index in dataframe1.index:
#     print(Index)
# for Columns in dataframe1.columns:
#     print(Columns)

# could use these methods to iterate over entire dataframe.

# Exercise 39 - Pandas DataFrames
# Write a program that creates a DataFrame consisting of at least 4 rows and 6 columns. The DataFrame should contain random numbers generated vis NumPy. Let the program create 6 new DataFrames by sorting the original DataFrame alongside the columns(d.sort_value()). Let the program print a description of the original DataFrame. What do these numbers mean?
# e.g.
#
# import pandas as pd
# import numpy as np
#
# dataframeY = pd.DataFrame(
#     np.random.randn(2, 4), index=["Test1", "Test2"], columns=list("ABCD"),
# )
# print(dataframeY)
# dataframeX = dataframeY.sort_values("A")
# print(dataframeX)
#
# ###########
#
# import pandas as pd
# import numpy as np
#
# dataframe1 = pd.DataFrame(
#     np.random.randn(4, 6),
#     index=["Test1", "Test2", "Test3", "Test4"],
#     columns=list("ABCDEF"),
# )
#
# print(dataframe1)
# dataframe2 = dataframe1.sort_values("A")
# print(dataframe2)
# dataframe3 = dataframe1.sort_values("B")
# print(dataframe3)
# dataframe4 = dataframe1.sort_values("C")
# print(dataframe4)
# dataframe5 = dataframe1.sort_values("D")
# print(dataframe5)
# dataframe6 = dataframe1.sort_values("E")
# print(dataframe6)
# dataframe7 = dataframe1.sort_values("F")
# print(dataframe7)
#
# print(dataframe1.describe())

#### BioPandas

# it is a bit cumbersome to work with PDB files in "modern" programming languages
# takes pandas to the structural biology world
# Working with molecular structures of bioloigcal macromolecules (from PDB and MOL2 files)in pandas. DataFrames is what BioPandas is all about
# Please installbiopandas with $ pip install biopandas via your terminal before tring to run the script below:

# BioPDB.py

#### Matplotlib

# Matplotlib is a comprehensive library for creating static, animateed, and interactive visualizations in Pythons
# Create publication quality plots.
# Make interactive figures that can zoom, pan,

#### argparse

# Makes it easy to write user-friendly command-line interfaces
# The program defines what arguments it requires.
# The argparse module also automatically generates:
# help messages
# usage messages
# issue errors

####  Exercise 40 - argparse

# write a program using the module argparse that takes some strings as input and concatenates these strings in the order of input to one new string.
# Add at least three other arguments besides the strings that modify the program in different ways.
# the program could add spaces or could reverse the order of the input strings for example.
