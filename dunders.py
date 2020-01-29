"""
Dunders

Definition: Dunders, short for "double underscore functions", refer to functions and keywords provided by Python that
 are reserved for special uses. They are called such because they have two underscores before and after the name.
 Dunders include Magic Methods which have special properties, many of them dedicated for operator overriding, as well
 as some other special variables. In this example, the Fraction class has multiple Magic Methods, and some other
 Dunders are shown off afterwards.

Further reading:
 https://docs.python.org/3.8/genindex-_.html
"""

from math import *
from functools import reduce

# =Generic Helper Functions=
def find_factors(num):
    return [num]+[i for i in range(ceil(num/2)+1, 1, -1) if num % i == 0][1:]

def find_gcf(num1, num2):
    smaller = min(num1, num2)
    larger = max(num1, num2)
    for i in find_factors(smaller):
        if larger % i == 0: return i
    return -1

def find_lcm(num1, num2):
    lcm = reduce((lambda x, y: x*y), set(find_factors(num1) + find_factors(num2)))
    return lcm, lcm/num1, lcm/num2



class Fraction:
    """This class is supposed to represent a fraction, made up of a numerator and a denominator."""

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # =Helper Functions=
    def simplify(self):
        gcf = find_gcf(self.numerator, self.denominator)
        if gcf == -1: return self
        return Fraction(self.numerator // gcf, self.denominator // gcf)

    def decimal(self):
        return self.numerator/self.denominator

    # =Magic Functions=
    def __add__(self, other): # Overrides self+other
        denominator, res1, res2 = find_lcm(self.denominator, other.denominator)
        return Fraction(int(res1 * self.numerator + res2 * other.numerator), denominator).simplify()

    def __eq__(self, other): # Overrides self==other
        self_simple = self.simplify()
        other_simple = other.simplify()
        return self_simple.numerator == other_simple.numerator and self_simple.denominator == other_simple.denominator

    def __ge__(self, other): # Overrides self>=other
        return self.decimal() >= other.decimal()

    def __pow__(self, power, modulo=None): # Overrides self**other
        return Fraction(self.numerator ** power, self.denominator ** power)

    def __neg__(self): # Overrides -self
        return Fraction(-1 * self.numerator, self.denominator)

    def __abs__(self): # Overrides abs(self)
        return Fraction(abs(self.numerator), abs(self.denominator))

    def __str__(self): # Overrides str(self)
        return f'{self.numerator}/{self.denominator}'

    def __repr__(self): # Overrides self.__repr__()
        return f'Fraction({self.numerator}, {self.denominator})'

    def __getattr__(self, item): # If the interpreter can't find attribute in object, it returns this.
        print(f'Sorry, {item} doesn\'t exist in Fraction')
        return 1

# =Testing Functions=
half = Fraction(1, 2)
third = Fraction(1, 3)
print(half + third)

two_quarters = Fraction(2, 4)
print(half == two_quarters)

print(half >= third)

print(half ** 2)

print(-half)

print(abs(-half))

print(half) # Print defaults to using str(self), and if __str__ does not exist, uses __repr__

print(half.__repr__()) # Repr is supposed syntactically be so that doing eval(obj.__repr__()) will return a new object

print(half.foo)

# =Other dunders=
print(half.__module__) # Returns the module scope that the object belongs to
print(half.__getattribute__('denominator')) # Alternate form of "half.denominator", used for dynamic getting
print(half.__dict__) # Returns the states that belong to the object
print(half.__class__) # Returns the class the the object is
print(Fraction.__dict__) # Returns the methods that belong to the class and class meta attributes
print(Fraction.__bases__) # Returns tuple of the base classes
print(Fraction.__doc__) # Returns the docstring (any string started with three double quotations right after function declaration)
print(Fraction.__name__) # Returns the name of the Class, useful (and dangerous) for dynamic things
print(__name__) # Returns the name of the module scope