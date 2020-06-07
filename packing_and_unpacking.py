"""
Argument Unpacking

Definition: One of the primary uses of the splat operator (*) is to pack and unpack arguments in a function to get
 an arbitrary number of them

Examples: args, kwargs
"""

numbers = [1, 2]
print(numbers) # This is the list
print(*numbers) # This is when the list is unpacked, which is equivalent to print(numbers[0], numbers[1])
a, b = numbers # For the record, if the number of unpacked variables == number of elements in list, this also unpacks
print(a, b)


# Manually setting arguments limits the number of arguments for each function
def add4Numbers(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4

print(add4Numbers(5, 47, 98, 20))



# By using the splat operator, the number of arguments can be arbitrary
def addAnyNumbers(*args):
    print(args)
    print(*args)
    return sum(args)

print(addAnyNumbers(2, 3, 47, 98, 20))


# kwargs are if the argument has keywords, also called named parameters
def myFunction(**kwargs):
    print(kwargs)
    [print(f"Argument {num}: {arg[0]} = {arg[1]}") for num, arg in zip(range(len(kwargs)), kwargs.items())]

myFunction(Alice=58, Bob=49)
print('Hello', end='')