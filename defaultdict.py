"""
Defaultdict

Definition: A class in the collections library from Python >2.5 that when a key is encountered for the first time,
 will automatically use the factory of the provided value type to create the key-value pair. This is useful for when
 making a new dict from data and not having to write exceptions to see if the key already exists.
"""

filetext = \
"""alice bob
bob charlie
dave bob
erin alice"""

# Original way of doing it:
badDict = {}
for line in filetext.splitlines():
    friend1, friend2 = line.split(' ')
    if friend1 in badDict:
        badDict[friend1] += [friend2]
    else:
        badDict[friend1] = [friend2]
    if friend2 in badDict:
        badDict[friend2] += [friend1]
    else:
        badDict[friend2] = [friend1]

# Now with defaultdict
from collections import defaultdict
goodDict = defaultdict(list)
for line in filetext.splitlines():
    friend1, friend2 = line.split(' ')
    goodDict[friend1] += [friend2]
    goodDict[friend2] += [friend1]

print(badDict)
print(dict(goodDict)) # Must cast from defaultdict class back into a dict
# These are the same