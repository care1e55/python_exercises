
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
