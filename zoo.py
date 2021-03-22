from dataclasses import dataclass

@dataclass
class Animal():
    number_of_legs = None
    color = None
    species = None

    def __repr__(self) -> str:
        return f'{self.color.title()} {self.species}, {self.number_of_legs} legs'

# @dataclass
class Sheep(Animal):
    species = 'sheep'
    number_of_legs = 4

    def __init__(self, color='white'):
        self.color = color


@dataclass
class Wolf(Animal):
    species = 'wolve'
    number_of_legs = 4
    color: str = 'gray'

    def __repr__(self):
        return super().__repr__()



@dataclass
class Snake(Animal):
    species = 'snake'
    number_of_legs = 0
    color: str = 'green'

    def __repr__(self) -> str:
        return super().__repr__()


@dataclass
class Parrot(Animal):
    species = 'parrot'
    number_of_legs = 2
    color: str = 'red'
    
    def __repr__(self) -> str:
        return super().__repr__()


class Cage():
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *animals):
        for animal in animals:
            self.animals.append(animal)

    def __repr__(self):
        return "\n".join(animal.__repr__() for animal in self.animals)


if __name__ == '__main__':
    s1 = Sheep()
    s2 = Sheep('black')
    w = Wolf()
    p = Parrot()
    c = Cage(1)
    c.add_animals(s1, s2, w, p)

    print(s1, s2, w, p, sep='\n')
    print(c)
    print(id(w))
