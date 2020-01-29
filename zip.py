"""
Zip

Definition: One of the great beauties of Python. One simple function makes so many one-liners possible. Zip creates an
 iterable from pairing together one or more iterables.
"""

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
print(list(zip(numbers, letters))) # Two lists are combined to make a 2-d list
print(dict(zip(letters, numbers))) # It can also make a dict, where the key is from the first list and the values from the second
print(dict(zip({'a': 1, 'b': 2}, [3, 4]))) # Additionally, it can be used to totally overwrite a dict

print(list(zip(['a'], [1, 2])))
print(list(zip(['a', 'b'], [1]))) # Zip makes an iterable the size of the smallest argument

numbers, letters = zip(*[(1, 'a'), (2, 'b')])
# To unzip is to simply zip again, but the argument must be unpacked since zip takes multiple arguments, not a single list
print(f'{numbers=}, {letters=}')
print(list(zip(*list(reversed(list(zip(*[(1, 'a'), (2, 'b')])))))))
# Which means it's possible to switch the order of pairs in a list by unzipping, reversing, then zipping it back


# Let's say we get this CSV of days and four points of temperature in fahrenheit for each
csv = \
"""day_of_week,6:00,12:00,18:00,24:00;
Monday,73,77,77,74;
Tuesday,72,74,75,73;
Wednesday,74,79,77,75;"""

# Now for two lines of absolute Python shenanigans
title, *data = csv.split(';\n') # Refer to 'advanced_indexing.py'
# To understand this, know about comprehensions and the fact that in Python, 'truthy and truthy' returns the second truthy
print({day['day_of_week']: day.pop('day_of_week') and day for day in [dict(zip(title.split(','), row.split(','))) for row in data]})
# Ta-da, now the CSV has been converted to a very nice dict!