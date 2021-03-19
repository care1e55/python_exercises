from typing import List
from dataclasses import dataclass, field

@dataclass
class Scoop():
    flavor: str


@dataclass
class Bowl():
    bowl: List[Scoop] = field(default_factory=list)

    def add_scoops(this, *args):
        this.bowl += [*args]

    def __repr__(this) -> str:
        return ", ".join(scoop.flavor for scoop in this.bowl)


def create_scoops() -> List[str]:
    return [
        Scoop('chocolate'),
        Scoop('vanilla'),
        Scoop('persimmon'),
    ]


if __name__ == "__main__":
    print(create_scoops())
    s1, s2, s3 = Scoop('chocolate'), Scoop('vanilla'), Scoop('persimmon')
    b = Bowl()
    b.add_scoops(s1)
    b.add_scoops(s3, s2)
    print(b)
