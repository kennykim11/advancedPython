"""
Dataclasses

Definition: A module in Python >3.7 that predefines several special methods to custom classes. Is useful when wanting to
 create well-defined functions quickly. It by default defines the __init__, __repr__, and __eq__ functions, and also has
 the capability to define a __hash__ function and any order functions like __lt__, __ge__, etc.
"""

from dataclasses import dataclass, field

@dataclass(unsafe_hash=True)
class Character:
    displayName: str
    health: int

@dataclass(unsafe_hash=False)
class Warrior(Character):
    faction: str
    rank: str = field(default='private')
    # Equal to "rank: str = 'private'", but use then when needing to set other things in field
    weapons: list = field(default_factory=list)
    # Dataclasses do not allow mutable defaults because it cannot generate that code. Also it's probably not intended
    militaryId: str = field(default='', repr=False) # Do not display when calling __repr__


joe = Character("Joe", health=10)
 # The __init__ function defined by dataclass requires values for all fields in the class. These can be positional.

print(joe) # It is only possible to print an object of this class because dataclass has defined the __repr__ function

gi_joe = Warrior('GI Joe', 10, 'GI Joe Team')
 # Since Warrior extends Character, all the fields for Character must be provided, then all required fields for Warrior
print(gi_joe) # The militaryId field does not show when calling __repr__ because its field object has repr=False

print(hash(joe)) # The hash function is defined because the dataclass unsafe_hash is True for Character
print(hash(gi_joe)) # It does not work for Warrior because unsafe_hash is False. Also, lists are not hashable.