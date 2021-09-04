# Итак, у вас есть корзина с грушами и несколько детей. Нужно поделить груши так,
# чтобы никому из детей не было обидно, то есть поровну. (Теперь понятно, почему в задаче дети?)
# Напишите класс PearsBasket,
# экземпляр которого при инициализации получает целое число – количество груш в корзине.
# В классе должны быть методы:
#
# pb // n – деление нацело, возвращает список объектов класса
# со значениями количества груш в каждой корзинке,
# если есть остаток – он должен находиться в дополнительной последней корзинке.
# pb % n – получение остатка от деления, возвращает число: остаток от деления.
# pb_1 + pb_2 – складываются две корзинки, получается новая корзина;
# pb_1 - n – число вычитается из корзинки, если там есть такое количество груш;
# если нет – вычитается сколько есть, остается 0;
#  __str__ – возвращает количество груш в корзине;
#  __repr__ – возвращает строку в формате PearsBasket(<количество>).


class PearsBasket():

    def __init__(self, pears: int):
        self.pears = pears

    def __add__(self, other):
        return PearsBasket(self.pears + other.pears)

    def __sub__(self, other):
        self.pears -= other
        return self

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
        return str(self.pears)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.pears})"


