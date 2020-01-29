"""
Dir and vars

Definition: dir() and vars() are two ways to get the fields and methods of a class or object. Like many things in
 Python, they do similar things but are slightly different. Using these methods can be especially helpful when
 trying to understand a new module or library.
"""

class Character:
    def __init__(self, name):
        self.name = name


class Droid(Character):
    """These are the droids you're looking for"""

    poweredOn = True

    def introduce(self):
        if self.poweredOn:
            print(f'I am {self.name}, human-cyborg relations.')


print(sorted(dir(Droid))) # dir() lists all the possible functions that can be called on the class and all static fields of the class
print(sorted(list(Droid.__dir__(Droid('C-3PO'))))) # __dir__ returns all the same things as dir() but also lists the object's fields and methods

print(vars(Droid)) # Lists fields and methods of the class
print(Droid.__dict__) # Gives the same thing as vars
print(vars()) # With no argument, vars prints the attributes of the current module

# Some other useful info:
print(Droid.__doc__) # Gives out only the documentation which is always the triple double-quoted string right after the class or function header
print(Droid.__name__) # Gives the name of the Class
print(Droid.__module__) # Gives what module it is a part of
print(Droid.__bases__) # Gives superclass of the class