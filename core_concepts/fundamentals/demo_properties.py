#!/usr/bin/env python3


class Person:
    """
    propery -> hybrid between method and attribute
    """

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        # getter method should not take any argument
        return f'{self.first} {self.last}'

    @full_name.setter
    def full_name(self, value):
        self.first, self.last = value.split(" ")


class Ticket:
    __price: int  # hiding this valiable from user, restricting the access only via getter and setter

    def __init__(self, price):
        # self.__price = price
        self.price = price  # call setter method to reuse validation logic

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        """setter with validation logic"""
        # reuse the validation logic during the creating of that object
        if new_price < 0:
            raise ValueError(f"nice try with {new_price}")
        self.__price = new_price


class Money:
    dollars: int
    cents: int

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents


class Moneyv2:
    _total_cents: int

    def __init__(self, dollars, cents):
        """
        this changed outer interface of that class completely by removing the protected dollar and cents variable
        if those valiables are public and protected then other devs are using that and this change breaks their code
        """
        self._total_cents = dollars * 100 + cents


class Moneyv3:
    total_cents: int

    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    # recreate the dollar and cents dynamically
    @property
    def dollar(self):
        return self.total_cents // 100

    @dollar.setter
    def dollar(self, new_dollars):
        self.total_cents = 100 * new_dollars + self.cents  # use the getter of cents

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, new_cents):
        self.total_cents = 100 * self.dollar + new_cents  # use the getter of dollar


if __name__ == "__main__":
    ticket = Ticket(10)
    print(ticket._Ticket__price)  # name mangled rule appiled for private variable
    print(ticket.price)

    ticket.price = 100
    print(ticket.price)
    print(ticket._Ticket__price)

    ticket._Ticket__price = 150
    print(ticket._Ticket__price)
    print(ticket.price)

    ticket.price = -1

    exit(0)

    ravi = Person("Ravi", "Giri")
    print(ravi.full_name)  # full_name is a dynamic attribute which value is calculated at run time,
    # it is not a method anymore, readOnly pattern if setter is not implemented
    ravi.full_name = "Chenkai Gao"
    print(ravi.full_name)
