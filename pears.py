class PearsBasket():

    def __init__(self, pears: int):
        self.pears = pears

    def __add__(self, other):
        return self.pears + other.pears

    def __sub__(self, other):
        self.pears -= other
        self.pears = max(0, self.pears)
        return self.pears

    def __floordiv__(self, other):
        amount_in_basket = self.pears // other
        remainder = self.pears % other
        if remainder:
            return [PearsBasket(amount_in_basket) for _ in range(other)] + \
                [PearsBasket(remainder)]
        return [PearsBasket(amount_in_basket) for _ in range(other)]

    def __mod__(self, other):
        return self.pears % other

    def __str__(self):
        return self.pears

    def __repr__(self):
        return f"{self.__class__.__name__}({self.pears})"
