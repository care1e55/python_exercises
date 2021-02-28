
class AbstractCat():

    food_limit = 100

    def __init__(self):
        self.eaten = 0
        self.weight = 0

    def eat(self, food):
        self.eaten += food
        self.weight = self.eaten // 10
        self.weight = min(self.weight, self.food_limit)

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.weight})"


class Kitten(AbstractCat):
    def __init__(self, weight):
        self.weight = weight
        self.eaten = weight * 10

    def sleep(self):
        return "Snore" * (self.weight // 5)

    def meow(self):
        return 'meow'


class Cat(Kitten):
    def __init__(self, weight, name: str):
        self.weight = weight
        self.eaten = weight * 10
        self.name = name

    def get_name(self):
        return self.name

    def meow(self):
        return 'MEOW...'

    def catch_mice(self):
        return 'Got it!'
