#!/usr/bin/env python3

from dataclasses import dataclass, field


class Person:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f'{self.first} {self.last}'

    def __str__(self):
        """user friendly representation"""
        return f'{self.first} {self.last} {self.age}'

    def __repr__(self):
        """machine frirndly representation. recreate the object with its current state"""
        # a string that can be evaluated as python code and recreate the object
        return f'Person({self.first}, {self.last}, {self.age})'

    def __eq__(self, other):
        return self.first == other.first and self.last == other.last and self.age == other.age


@dataclass
class Personv2:
    """
    - no need to wrire boiler plate constructor
    - order matters
    - variable type hints
        - it is just used for documentation
        - python does not enforce it instead it acts as a foundation for other tools like dataclass
        - but dataclass does not use it.
        # __init__() is free
    - if you write your own constructor then it seems overiding the generated one but actually
    - the dataclass generator checks if any constructor is present then it will not create further
    - it adds the __repr__() -> free NOT __str__() -> you need to define it
    - __eq__() -> free, but it does order wise evaluation
    """
    first: str
    last: str
    age: int

    def full_name(self):
        return f'{self.first} {self.last}'


@dataclass(order=True)
class Money:
    # dollars: int
    dollars: int = field()
    # cents: int = 10
    cents: int = field(default=10)

    def __post_init__(self):
        # executes after the automatic constructor that sets up the member variables
        if self.cents > 100:
            self.dollars += self.cents // 100
            self.cents = self.cents % 100

    def __str__(self):
        return f'${self.dollars}.{self.cents:02d}'

    def __repr__(self):
        return f'Money({self.dollars}, {self.cents})'


class Department:
    def __init__(self, name, inventory=[]):  # bug: at byte compile type it creates an empty list so every instance
        # gets the same list
        self.name = name
        self.inventory = inventory


class Departmentv2:
    def __init__(self, name, inventory=None):
        # fix the bug
        if inventory is None:
            inventory = []
        self.name = name
        self.inventory = inventory


@dataclass
class Departmentv3:
    name: str = field()
    # inventory: list = [] -> throws ValueError
    inventory: list = field(default_factory=list)
    # default_factory uses callable to generate a new value each time when the class is instanciated


if __name__ == "__main__":
    cse = Department("cse")
    cse.inventory.append("asinha")
    ee = Department("ee")
    ee.inventory.append("ghatang")

    print(cse.inventory)  # ghatang is added

    cse = Departmentv2("cse")
    cse.inventory.append("asinha")
    ee = Departmentv2("ee")
    ee.inventory.append("ghatang")

    print(cse.inventory)  # ghatang is not added

    cse = Departmentv3("cse")
    cse.inventory.append("asinha")
    ee = Departmentv3("ee")
    ee.inventory.append("ghatang")

    print(cse.inventory)  # ghatang is not added

    amount = Money(142, 7)
    print(str(amount))
    print(amount)
    print(repr(amount))

    a = Money(1, 5)
    b = Money(0, 105)
    print(a > b)  # evaluates False coz it does -> self.dollers > other.dollers and self.cents > other.cents
    # for the actual results compare with total_cents
    print("")

    chen = Person('Ravi', 'Giri', 28)
    print(chen.full_name())
    # when dunder repr is implemented the code then repr() is
    print((str(chen)))  # str() is not a function, it is build in type, it is callable, print() interns calls it

    ravi = Person('Ravi', 'Giri', 28)
    print(ravi.full_name())

    print(ravi == chen)  # with out the __eq__() implementation, returns False coz both are different obj

    a = Personv2("Abhijit", "Sinha", 38)
    b = Personv2("Abhijit", "Sinha", 38)

    print(a == b)  # by default adds the __repr__()
