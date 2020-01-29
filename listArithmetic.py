"""
List Arithmetic

Definition: Use addition and multiplication to add to lists

Uses: exploitation payloads, lists with initial values
"""

print([5, 7] + [10])
numbers = [1, 2, 3]
numbers += [4, 5] # This is equivalent to numbers.append(4); numbers.append(5);
print(numbers)

print([8] * 10)
print([1, 2] * 10) # Can multiple multiple elements
print([[1, 2]] * 10) # Now that this is encapsulated in a list, the list is multiplied, not the elements

print("Hello, " * 5) # Since strings are iterable too