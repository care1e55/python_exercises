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


if __name__ == '__main__':
    s1 = Sheep()
    s2 = Sheep('black')
    w = Wolf()
    p = Parrot()

    print(s1, s2, w, p, sep='\n')
