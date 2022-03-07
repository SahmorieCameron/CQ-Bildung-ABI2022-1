import random

print("Inner and Outer functions")


def outer(a, b):
    def inner(a, b):
        inner = a + b
        return inner

    outer = (inner(a, b)) + (a ** 2)
    return outer


a = random.randint(0, 5)
b = random.randint(0, 5)
print(f"Our randomly selected integers are {a} and {b}")
result1 = outer(a, b)
print(f"Using our functions the result is {result1}")

# Loops

x = int(input("Please give us a number to sum: "))
sum = 0
for i in range(0, x):
    sum = sum + i
print("The sum is " + str(sum))

# Dictionaries
print("Dictionaries")
sample_dict = {"a": 100, "b": 200, "c": 300}

some_key = "b"
if some_key in sample_dict:
    print("Key exists")
else:
    print("Key doesn't exist")
if 150 in sample_dict:
    print("Value exists")
else:
    print("Value not present")

sample_dict2 = {
    "emp1": {"name": "Jhon", "salary": 7500},
    "emp2": {"name": "Emma", "salary": 8000},
    "emp3": {"name": "Brad", "salary": 500},
}
print(sample_dict2)

sample_dict2 = {
    "emp1": {"name": "Jhon", "salary": 7500},
    "emp2": {"name": "Emma", "salary": 8000},
    "emp3": {"name": "Brad", "salary": 8500},
}
print(sample_dict2)
