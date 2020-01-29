"""
Walrus Operator

Defintion: The "walrus operator" is a new operator in Python 3.8 that allows assignment while evaluating. These can
 be placed in if, for, and while conditionals, as well as some definitions.
"""

# FROM https://www.python.org/dev/peps/pep-0572/

# Handle a matched regex
if (match := pattern.search(data)) is not None:
    # Do something with match

# A loop that can't be trivially rewritten using 2-arg iter()
while chunk := file.read(8192):
   process(chunk)

# Reuse a value that's expensive to compute
[y := f(x), y**2, y**3]

# Share a subexpression between a comprehension filter clause and its output
filtered_data = [y for x in data if (y := f(x)) is not None]