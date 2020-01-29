"""
Lambdas

Definition: A lambda is a shorthand way of writing a writing a function. These are useful for when providing a function
 as an argument, for example the default map and sort functions.
"""

# Map takes in a function as the first argument, so a lambda can be passed in
print(list(map(lambda x: abs(x), [-3, 5, -8])))
# Also equivalent to "print(list(map(abs, [-3, 5, -8])))"

# This would be the long way:
