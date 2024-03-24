class Money:
    dollars: int
    cents: int

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    @staticmethod
    def factory_func_money_from_cents(total_cents):  # hacky way to support Polymorphic constructor
        # wrapper function to return a Money class object
        # this function is not attached or encapsulated with the class
        dollars = total_cents // 100
        cents = total_cents % 100
        return Money(dollars, cents)  # problem: change Money -> TipMoney or similar for each subclass

    @classmethod
    def from_cents(cls, total_cents):
        dollars = total_cents // 100
        cents = total_cents % 100
        return cls(dollars, cents)  # resolve the provious problem by using cls

    def __str__(self):
        return f'${self.dollars}.{self.cents}'


class TipMoney(Money):
    pass


if __name__ == "__main__":
    a = Money(10, 5)
    print(a)
    b = Money.factory_func_money_from_cents(1005)  # python does not allow Polymorphic constructor
    print(b)

    c = TipMoney.factory_func_money_from_cents(1020)
    print(c)
    d = TipMoney.from_cents(1020)
    print(d)
