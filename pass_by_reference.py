"""
Pass by reference

Definition: There is a ton of confusion in the Python world about whether Python is pass by value or reference. While
 it is mostly pass by reference, it is not purely so, since assigning a variable to an immutable will result in the
 variable being reassigned, not overwritten. Additionally, all variables are passed by reference to functions.
"""


def change(x):
    old_id = id(x) # Saving the old id
    if type(x) == int: x = 5 # Replacing
    if type(x) == list: x += [5] # Pushing to list
    if type(x) == str: x += "bar" # Concatenating to string
    return old_id, id(x) # Sending the new and old id

x = 3
print(id(x), *change(x))

y = [3]
print(id(y), *change(y)) #Since lists are mutable, the list was changed and the reference was never reassigned

z = "foo"
print(id(z), *change(z)) #Although string concatenation seems like a mutation, it actually creates a new string

#One interesting thing to note is that since all variables are references, Python is smart to share references between
# immutables but not mutables when the values are the same
int1 = 1234
int2 = 1234
int3 = 1230
int3 += 4 # Even though int 3 now equals 1234...
print(id(int1), id(int2), id(int3)) # ... it does not get replaced by already existing reference for 1234

list1 = []
list2 = []
print(id(list1), id(list2))