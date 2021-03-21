from typing import List
from dataclasses import dataclass, field

@dataclass
class Scoop():
    flavor: str


@dataclass
class Bowl():
    bowl: List[Scoop] = field(default_factory=list)
    max_scoops = 3

    def add_scoops(this, *new_scoops):
        for scoop in new_scoops:
            if len(this.bowl) < this.max_scoops:
                this.bowl.append(scoop)

    def __repr__(this) -> str:
        return ", ".join(scoop.flavor for scoop in this.bowl)


class BigBowl(Bowl):
    max_scoops = 5


def create_scoops() -> List[str]:
    return [
        Scoop('chocolate'),
        Scoop('vanilla'),
        Scoop('persimmon'),
    ]


if __name__ == "__main__":
    s1, s2, s3 = Scoop('chocolate'), Scoop('vanilla'), Scoop('persimmon')
    b = Bowl()
    bb = BigBowl()
    bb.add_scoops(s1)
    print(bb.bowl)
    bb.add_scoops(s3, s2)
    bb.add_scoops(s3, s2)
    bb.add_scoops(create_scoops())
    print(bb)
