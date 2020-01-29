"""
Comprehensions

Definition: A short way of iterating through an iterable and producing the result in the same type.
    Overused go-to for people to say they know Python really well

Uses: Modifying each element in an iterable

Related: For loops, lambdas, ternary, lambdas
"""

print([x ** 2 for x in range(5)]) # List
"""
Equivalent to:
    listOfNums = []
    for x in range(5):
        listOfNums += [x ** 2]
    print(listOfNums)
"""
print({x ** 2 for x in range(5)}) # Set
print({x: x ** 2 for x in range(5)}) # Dict
squareGen = (x ** 2 for x in range(5)) # Generator
print(squareGen)
print(list(squareGen))

numbers = list(range(5))
print([y + x for x,y in zip(numbers, numbers[1:])])

print([x ** 2 if not x % 2 else None for x in range(5)]) # Can use ternaries
print([x ** 2 for x in range(5) if not x % 2]) # You don't have to use an else if you move the if

studentGrades = {"Kenny":[56, 72, 49], "Owen":[93, 87, 96]}
print({name: [grade + 10 for grade in grades] for (name,grades) in studentGrades.items()}) #You can also do a nested comprehension
print({name: [grade + 10 if grade + 10 <= 100 else 100 for grade in grades] for (name,grades) in studentGrades.items()}) #And now an ternary

# There is also this legnedary hack for hacking from a 2D array into a 1D: https://stackoverflow.com/questions/952914
l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
print([item for sublist in l for item in sublist])

# As of 3.8, you can now use dict comprehensions to compile inputs as a dict (you could in previous versions but value came first)
people = {input('What is your name? '): input('What is your age? ') for i in range(2)}
print(people)