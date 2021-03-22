from dataclasses import dataclass
from typing import List

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


class Zoo():
    def __init__(self):
        self.cages = []

    def add_cages(self, *cages):
        for cage in cages:
            self.cages.append(cage)

    def animals_by_color(self, color) -> List[Animal]:
        return [
            animal for cage in self.cages for animal in cage.animals if animal.color == color
        ]


    def animals_by_legs(self, num_legs) -> List[Animal]:
        return [
            animal for cage in self.cages for animal in cage.animals if animal.number_of_legs == num_legs
        ]

    def number_of_legs(self) -> int:
        return sum(animal.number_of_legs for cage in self.cages for animal in cage.animals)


    def __repr__(self):
        "Print all the cages"
        return "\n".join(cage.__repr__() for cage in self.cages)


if __name__ == '__main__':
    s1 = Sheep()
    s2 = Sheep('black')
    w = Wolf()
    p = Parrot()
    c1 = Cage(1)
    c2 = Cage(2)
    c1.add_animals(w, p)
    c1.add_animals(s1, s2)

    z = Zoo()
    z.add_cages(c1, c2)

    print(s1, s2, w, p, sep='\n')
    print(c1)
    print(c2)
    print(id(w))
    print('====================================')
    print(z.number_of_legs())
    print(z.animals_by_color('white'))
    print(z)



