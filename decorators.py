"""
Decorators

Definition: Decorators are functions that extend the behavior of a target function, by returning a result function that
 calls the target inside of it. Python will know to call the result function and not the target function. Decorators
 can also extend the behavior of a target class.
"""

from time import time

# For example, this function times how long a function takes to run
def time_it(func):
    start_time = time()
    func()
    print(f'The function "{func.__name__}" took {round(time() - start_time, 10)} seconds.')


# This would be the way to use the time_it function without a decorator
def test_1():
    var = 10 ** 17 + 1234
time_it(test_1)
# This works for running one time, but there may be cases when it would be desired to redefine test_1 to include the
#  functionality of time_it. In that case, time_it must return the function that contains the behavior of time_it.



# This is the equivalent way of using a decorator
def time_it_deco():
    def timer(func):
        start_time = time()
        func()
        print(f'The function "{func.__name__}" took {round(time() - start_time, 10)} seconds.')
    return timer

@time_it_deco
def test_2():
    var = 10 ** 17 + 1234
test_2() # This time, wrapping the function call in another function call is not needed.



# Code from here: https://www.geeksforgeeks.org/decorators-in-python/
def decorator(*args, **kwargs):
    print("Inside decorator")

    def inner(func):
        print("Inside inner function")
        print(func)
        print("I like", kwargs['like'])
        return func

    return inner


@decorator(like="geeksforgeeks")
def tester():
    print("Inside actual function")


tester()