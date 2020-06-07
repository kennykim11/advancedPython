"""
Global and nonlocal

Definition: These are ways to interact with variables outside of the current scope. Declaring a variable to be global
 means that it references the variable with that name in the first scope of the module. Declaring it non-local means
 that it references the variable with that name only in the scope that is a single layer outside. Funnily, global
 is not truly program-global, it is module-global. either way, there is almost never a good reason to use global and
 nonglobal, since it can make debugging much more of a headache. If you need multiple variables changed, pass it in the
 function, then return the changes in a list and instantly unpack it.
"""

a = 4

def foo():
    global a
    a = 5 # This is able to mutate the global a since it has been declared global
foo()
print(a)

def bar():
    a = 6
    def barbar():
        nonlocal a # This mutates the a of bar(), not of the module's scope
        a = 7
    barbar()
    print(a)
    def barbarbar():
        global a # This mutates the a of the module's scope, and not the a of bar()
        a = 8
    barbarbar()
    print(a) # See?
bar()
print(a)

# Not to be confused with the globals function, which returns a dictionary representing the variables, functions, and details of the module's scope
print(globals())