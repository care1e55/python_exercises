from dataclasses import dataclass


def polynomial_derivative(polynomial: str):
    pass


@dataclass
class PolynomMember:
    multiplier: int
    power: int

    def derivative(self):
        return PolynomMember(
            multiplier=self.multiplier,
            power=self.power-1
        )

    def __str__(self):
        return f'{self.multiplier}x^{self.power}'


class Polynom:

    def __init__(self, members):
        self.members = members

    @classmethod
    def from_str(cls, polynomial: str):
        str_members = polynomial.split('+')
        return cls(cls.parse_member(str_member) for str_member in str_members)

    def __str__(self):
        return "+".join(str(member) for member in self.members)

    @staticmethod
    def parse_member(str_member: str) -> PolynomMember:
        multiplier, power = tuple(member.strip() for member in str_member.split('x'))
        multiplier = '1' if not multiplier else multiplier
        power = '^1' if '^' not in power else power
        return PolynomMember(multiplier=int(multiplier), power=int(power[1:]))

    def derivative(self):
        return Polynom([member.derivative() for member in self.members])


if __name__ == '__main__':
    test_polynomial = "2x^2 + x"
    print(Polynom.from_str(test_polynomial))
    print(Polynom.from_str(test_polynomial).derivative())
