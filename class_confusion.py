"""
Class confusion

Definition: Especially for those coming from Object Oriented languages like Java, Python's class system can cause some
 confusion. Very small details can drastically change how a class operates. There's a couple rules to always keep in
 mind:
  1. Objects do not necessarily strictly follow the class structure
  2. Class attributes are static and shared between all objects of the class. For object-individual attributes, use
   __init__ and declare self.<attribute>
  3. Both objects and classes are not protected from mutations
"""

class Course:
    id: str
    maxCapacity = 20
    students = []
    tas: list

    def __getattr__(self, item): # This gets called if the attribute does not exist
        return f'There is no attribute called {item}'


a = Course()
a.students += ["Kenny"]
a.tas = ["Kyle"]
a.id = "5"
a.maxCapacity = 35

b = Course()
print(b.students) # b shares the same students as a
print(b.tas) # But b does not have the same tas as a
print(b.id) # Nor the same id
print(b.maxCapacity) # b has a maxCapacity, but it is not the same as a

Course.id = "8" # Changing the field of the Course class, not a Course object
c = Course() # What happens when making a totally new Course?
print(a.id, b.id, c.id) # Both b and c adopted the new Course id, but a did not