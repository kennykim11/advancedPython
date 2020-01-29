"""
Generators

Definition: Generators are a way of creating iterators without having to store the entire result of the iterator in
 memory. These are very good when the data involved can theoretically get large, for example, reading a file one line
 at a time.
"""

def fibonacci():
    cache = [0, 1] # [total, last total]
    while True:
        cache = [cache[0] + cache[1], cache[0]] # Change cache
        yield cache[0] # Return total

while True:
    for element in fibonacci(): # Goes on infinitely
        input('')
        print(element, end='')