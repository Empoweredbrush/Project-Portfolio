

# List comprehension to find top earners

# Basics

#the code below contains a dictionary that goes through a simple loop that compares the different values in the dictionary and any that are greater than 100000 are added to the top earners list. Once done it then prints top earners.

employees = {
    'Alice': 100000,
    'Bob': 99817,
    'Carol': 122908,
    'Frank': 88123,
    'Eve': 93121}

top_earners = []
for key, val in employees.items():
    if val >= 100000:
        top_earners.append((key, val))

print(f"before the one liner {top_earners}")

# [('Alice', 100000), ('Carol', 122908)]

# though the code above does what we want, it isn't as readable and concise as it could be. So below we will be utilizing list comprehension to make it more readable and concise.

# list comprehension is as thus: [ expression + context] 
# example: [x * 2 for x in range(3)], x * 2 is the expression and for x in range(3) is the context.

employees = {
    'Alice': 100000,
    'Bob': 99817,
    'Carol': 122908,
    'Frank': 88123,
    'Eve': 93121}

top_earners = [(k, v) for k, v in employees.items() if v >= 100000]

print(f"After one liner {top_earners}")

# nothing has changed but the code is cleaner and easier to read. the output the same, though the difference being we have added list comprehension, that being our loop straight into top earners. (k, v) being the expression where for k, v in employees.item if v >= 100000 being the context.

# lets test it out on our own.

# lets use a list that takes numbers from 1 to ten but we square each one.

squared_numbers = [x**2 for x in range(1, 11)]

print(f"Squared numbers from 1 to 10: {squared_numbers}")

# now lets take that list and try to do factorials of each number using recursion but the numbers are randomly generated.

import random

squared_integers = [random.randint(1, 10) for _ in range(20)]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
factorials = [factorial(x) for x in squared_integers]

print(f"Random squared integers: {squared_integers}")
print(f"Factorials of those integers: {factorials}")