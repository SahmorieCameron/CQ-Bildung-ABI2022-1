# #### Functions
#
# # Programmers hate repeating things
#
# # The Signature
#
# # The signature describes the name of the function, which parameter/s it uses and which data type
# # the return value
#
# # Parameters
#
# # Functions in most cases need parameters
# # Are given to the function on call back
# # Determine how to use the function
# # Types and order of the parameters are dictated explicitly by the signature
# # Data types are fixed, but variable in the declaration e.g. direct numbers
# # Call back of a function with parameters of the wrong type leads to compiler errors
#
# # Programme execution
#
# # is like a normal instruction block.
#
# # Can call functions within a function.
# # IMPORTANT: All variables and structures within a function only exist as long as the function is run and are lost afterwards.
# # Therefore there is a workspace before, during and after running a function.
#
# # The feature def
#
# # In python functions are defined with the feature def:
# # the statement def is follwed by the name of the function with the parameters passed to functions in the brackets. The statemetns after a":" in the first line are executed when the function is used
# # This continues until either the idented statements end or a return is encountered.
#
#
# def sumup(a, b):  # SIGNATURE. sumup = function name.
#     sum = a + b  #
#     return (
#         sum  # return hands over variables to the main workspace. like a print command.
#     )
#
#
# ClcSum = sumup(6, 7)
# print(ClcSum)
#
#
# # Variables in Functions
#
# # When using functions you often have variables in this repeated code parts.
# # Python deals with them in a special way
# # So far we encountered global Variables
# # Functions use a special type called local Variables
# # these only exist when the function runs
# # When a local variable has the same name as another variable (e.g. a global variable), the local one hides the other.
#
# # Rules for functions
#
# # Try to avoid duplicate source code
# # A function should only be dependent on its parameters
# # one function is exactly 1 job
# # the source code shouldn't contain too many lines...
#
# #### Exercise 28 - Your first Functions
#
# # Create a program that defines functions for the four mathematical basic operations (+,-,* and /)
# # Call the functions at least three times with different parameters.
# import random
#
# print("Addition")
#
#
# def function1(a, b):
#     add = a + b
#     return add
#
#
# sum1 = 0
# sum2 = 0
# sum3 = 0
# for i in range(3):
#     sum1 = function1(random.randint(0, 100), random.randint(0, 100))
#     sum2 = function1(random.randint(0, 100), random.randint(0, 100))
#     sum3 = function1(random.randint(0, 100), random.randint(0, 100))
# print(str(sum1) + " " + str(sum2) + " " + str(sum3))
#
#
# def function2(a, b):
#     subtract = a - b
#     return subtract
#
#
# print("Subtraction")
# sum1 = 0
# sum2 = 0
# sum3 = 0
# for i in range(3):
#     sum1 = function2(random.randint(0, 100), random.randint(0, 100))
#     sum2 = function2(random.randint(0, 100), random.randint(0, 100))
#     sum3 = function2(random.randint(0, 100), random.randint(0, 100))
# print(str(sum1) + " " + str(sum2) + " " + str(sum3))
#
# print("Multiplication")
#
#
# def function3(a, b):
#     multiply = a * b
#     return multiply
#
#
# um1 = 0
# sum2 = 0
# sum3 = 0
# for i in range(3):
#     sum1 = function3(random.randint(1, 100), random.randint(1, 100))
#     sum2 = function3(random.randint(1, 100), random.randint(1, 100))
#     sum3 = function3(random.randint(1, 100), random.randint(1, 100))
# print(str(sum1) + " " + str(sum2) + " " + str(sum3))
#
# print("Division")
#
#
# def function4(a, b):
#     divide = a / b
#     if b == 0:
#         print("not possible")
#         return 0
#     divide = a / b
#     return divide
#
#
# for i in range(3):
#     sum1 = function4(random.randint(0, 100), random.randint(0, 100))
#     sum2 = function4(random.randint(0, 100), random.randint(0, 100))
#     sum3 = function4(random.randint(0, 100), random.randint(0, 100))
# print(str(sum1) + " " + str(sum2) + " " + str(sum3))
#
# #### Exercise 29 - Functions with simple Loops
#
# # Write a program that contains two different Functions
# # The first function should take a list as argument and return the sum of all elements in the list, calculated
# # by a loops.
# # The second function should also take a list and return a list in which the contents of the handed over lists over reversed
#
#
# randomlist = random.sample(range(0, 20), 5)
# print(randomlist)
#
#
# def function5(inputlist):
#     listsum = 0
#     for elem in inputlist:
#         listsum += elem
#     return listsum
#
#
# list1 = function5(randomlist)
# print("Here is the sum of our randomly generated list " + str(list1))
#
# #
# print()
#
# randomlist = random.sample(range(0, 20), 5)
# randomlist.sort()
# print(randomlist)
#
#
# def function6(inputlist):
#     revlist = []
#     for i in reversed(inputlist):
#         revlist += [i]
#     return revlist
#
#
# list2 = function6(randomlist)
# print("Here is our reverse list " + str(list2))

# Exercise 30 - Functions with nested Loops

# in Exercise 25, we worked with nested loops to find the maximum of a matrix, calculate the sum of all entries of a matrix and create a new matrix that is the result of element-wise multiplication of two other matrices
# Write a program that contains three different functions, one for each of the three tasks above

import random

matrix = [
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
]
print(matrix)

# ()
def function7(inputmatrix):
    sum = 0
    for i in range(len(inputmatrix)):
        for j in range(len(inputmatrix)):
            sum += inputmatrix[i][j]
    return sum


summatrix = function7(matrix)
print(summatrix)


print("Function for the maximal value of the matrix")


def function8(inputmatrix):
    max_value = 0
    for i in range(len(inputmatrix)):
        for j in range(len(inputmatrix[0])):
            if inputmatrix[i][j] >= max_value:
                max_value = inputmatrix[i][j]
    return max_value


maxmatrix = function8(matrix)
print("The maximum value is ", maxmatrix)

print(
    "Function for the multiplication of the components of two matrices in a third resulting matrix"
)


def function9(inputmatrix):
    newmatrix = []
    for i in inputmatrix[0]:
        for j in inputmatrix[1]:
            print(i, "*", j, "=", i * j)
            newmatrix.append(i * j)
    return newmatrix


trinitymatrix = function9(matrix)
print("New matrix is", trinitymatrix)
