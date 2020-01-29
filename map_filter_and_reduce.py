"""
Map, Filter, and Reduce

Definition: These are three functions in Python which take a function and a list to return something else.

See also: Comprehensions
"""

# Here's some data from a scientific instrument. Unfortunately, it wasn't perfect and it has put None's in the data.
data_points = [0, 2.673, None, 6.663, 10.361, 10.06, 8.473, 3.711, None, -0.87, 1.499, None, 1.872, -3.124, -4.912, -0.864, -2.85, -6.99, -10.27, -10.972, -15.028, None, -19.877, -18.182, -19.459]

# Take the None's out of the list with Filter
# Filter creates a new list, only including the elements of the argument list where the argument function returns a truthy value.
refined_data_points = list(filter(lambda x: x is not None, data_points))
print(refined_data_points)

# For some reason, the absolute values of each are required
# Map returns a list of the same length as the argument where function has been run on every element of the list
absolute_data_points = list(map(abs, refined_data_points))
# Equivalent to "list(map(lambda x: abs(x), refined_data_points))"
print(absolute_data_points)

# Now the sum of the data points is required
from functools import reduce
# Reduce applies a rolling computation to sequential pairs of values in a list.
data_sum = reduce((lambda x, y: x+y), absolute_data_points)
print(data_sum)