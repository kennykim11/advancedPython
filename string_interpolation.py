"""
String Interpolation

Definition: The evaluation of a string that has placeholders

Common uses: Debugging, making one-line print statements

Related:
"""

name = "Kenny"
age = 20

print("Hi my name is " + name + " and in two years, I will be " + str(age + 2)) # The boring way
print("Hi my name is", name, "and in two years, I will be", age+2) # Using commas will add a space and doesn't require explicit str casting
print(f"Hi my name is {name} and in two years, I will be {age+2}") # String interpolation, new in 3.6

print(f"{name=} {age=}") # String interpolation for debugging, new in 3.8
# Equivalent to print("name=" + name + " age" + str(age))