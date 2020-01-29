"""
Advanced Indexing

Definition: Python is one of the best languages for indexing in arrays.
"""

names = ["Alice", "Bob", "Chuck", "Dan", "Erin", "Frank", "Grace"]
print(names[3:7])
print(names[1:]) # == names[1:len(names)]

midpoint = len(names)//2
print(names[:midpoint], names[midpoint:]) # Effectively splits a list down the middle
print(names[::2]) # Skips every second item
print(names[1::2]) # Only gets every second item
print(names[1::-1]) # Excludes first and last item


# Can also be used for list copying
list1 = [1, 2, 3]
list2 = list1
list1[2] = 4
print(f'{list1=}, {list2=}') # The third element of both list1 and list2 changed
list2 = list1[:] # This is a Pythonic way to shallow copy
list1[1] = 5
print(f'{list1=}, {list2=}') # The second element of only list1 changed

# Can also use argument packing
*a, b = names
print(f'{a=}, {b=}')
a, *b = names
print(f'{a=}, {b=}')
a, d, *b, c = names
print(f'{a=}, {b=}, {c=}, {d=}')


# Lastly there is itemgetter from the operator library in the Python standard library to get multiple individual elements at once
from operator import itemgetter
getter = itemgetter(1,3) # Creates an itemgetter object that has a call dunder
print(getter(names))