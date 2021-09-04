# При наследовании классов класс-наследник обычно имеет больший функционал,
# чем родительский класс. А у котов все наоборот.
# Кошка по сравнению с котенком умеет ловить мышей (котенок пока нет)
# и мяукает громче (CAPS LOCK`ом). Поэтому логично кошку наследовать от котенка…
#
# Напишите классы:
#
# Класс АбстрактныйКот (AbstractCat), который инициализируется без аргументов. Умеет:
# – eat – есть. За каждые 10 единиц еды вес увеличивается на 1 единицу, пока не станет 100,
# дальше не растет. Если при одном приеме пищи количество еды не кратно 10,
# остаток запасается, а потом суммируется с новой едой.
# – возвращать строковое представление в виде <Имя класса> (вес).
#
# Класс Котенок (Kitten), наследуется от кота с аргументом вес. Умеет мяукать тоненько:
# – meow – возвращает строку "meow..."
# Еще умеет спать – sleep – возвращает строку Snore, повторенную столько раз,
# сколько число 5 помещается в весе.
#
# Класс Кошка (Cat), наследуется от котенка с аргументами вес и кличка.
# Умеет мяукать громко (meow):
# "MEOW..."
# и возвращать свое имя (get_name). Также умеет ловить мышей:
# – catch_mice – возвращает строку: Got it!

FOOD_LIMIT = 100


class AbstractCat():

    def __init__(self):
        self.weight = 0
        self.food_left = 0

    def eat(self, food):
        if self.weight <= FOOD_LIMIT:
            eaten = (food + self.food_left)
            self.food_left, weight_gain = eaten % 10, eaten // 10
            self.weight += weight_gain
            self.weight = min(self.weight, FOOD_LIMIT)

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.weight})"

    def __str__(self):
        return f"{self.__class__.__name__} ({self.weight})"


class Kitten(AbstractCat):

    def __init__(self, weight):
        super(Kitten, self).__init__()
        self.weight = weight

    def sleep(self):
        return "Snore" * (self.weight // 5)

    def meow(self):
        return 'meow'


class Cat(Kitten):
    def __init__(self, weight, name: str):
        super(Kitten, self).__init__(weight)
        self.name = name

    def get_name(self):
        return self.name

    def meow(self):
        return 'MEOW...'

    def catch_mice(self):
        return 'Got it!'
