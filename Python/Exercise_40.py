# -*- coding: utf-8 -*-
####  Exercise 40 - argparse

# write a program using the module argparse that takes some strings as input and concatenates these strings in the order of input to one new string.
# Add at least three other arguments besides the strings that modify the program in different ways.
# the program could add spaces or could reverse the order of the input strings for example.

"""
Created on Wed Feb 23 08:42:48 2022

@author: user
"""
import argparse

#### Setting up parser
parser = argparse.ArgumentParser(description="Concatenate strings.")
# Parser reads everything that comes into the commandline

### Positional arguments - only really need name, the destination and the type
parser.add_argument(
    "strings", metavar="S", type=str, nargs="+", help="strings to be concatenated"
)
# "strings" here is just a description, can be used later args.strings to access the strings
# metavar = just a name for the datatype within your help function
# type = Data type e.g. str for string, int for integer
# nargs = +,*,-,/ - it is plus here to it tells the program knows to add the string to a list.
# action="store_true" - as long as the user doesn't use the argument before it, the action doesn't activate.

#### Optional arguments!
parser.add_argument(
    "-p", "--print", action="store_true", help="print out the given strings"
)

parser.add_argument(
    "-s", "--space", action="store_true", help="adds space between words"
)

parser.add_argument(
    "-r", "--reverse", action="store_true", help="reverses the order of the strings"
)


parser.add_argument("")

#### The actual code
# must code the optional arguments using the names

args = parser.parse_args()
# ^ must be set

if args.reverse:
    args.strings = reversed(args.strings)

Bigword = ""
for word in args.strings:
    Bigword += word
    if args.space:
        Bigword += " "
print(Bigword)
