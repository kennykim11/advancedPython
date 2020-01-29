"""
Eval and Exec

Definition: In Python 3, the eval and exec functions are to interpret strings into Python code. Though there are slight
 differences in the two, they are both extremely powerful and unsecure.
"""

a = 3

print(eval('2 + a')) # Eval only evaluates a single expression and returns the value of that expression

print(exec('2 + a')) # Exec only runs the code inside and always returns None

exec('a = 2 + a') # For exec to return a value, it must have a statement setting something from the "outside" world
print(f'{a=}')