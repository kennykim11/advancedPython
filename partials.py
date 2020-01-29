"""
Partials

Definition: These are like Javascript's bind, but used less due to the nature of typical Python programs. These can be
 useful for callbacks or anything that takes a function as an argument.
"""

import functools

print_same_line = functools.partial(print, end='')
# In case you don't know, the end keyword argument defines what to append at the end of the string, the default is \n
print_same_line(5, 4)
print_same_line('Hello')
print_same_line(['World'])

# This is the equivalent if not using partials:
def print_same_line_func(*args):
    print(*args, end='')
print_same_line_func('Hello')


# Here is a more useful example:
import time
def do_this_later(seconds, function):
    time.sleep(seconds)
    function()

timeout = 3 # In this example, we want one number to contribute to both arguments of do_this_later
wait_three_seconds = functools.partial(do_this_later, timeout, lambda: print(f'\nThis ran after {timeout} seconds!'))
wait_three_seconds()