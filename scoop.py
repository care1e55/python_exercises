from typing import List

class Scoop():
    def __init__(this, flavor: str = None):
        this.flavor = flavor

    def __repr__(this) -> str:
        return this.flavor


class Bowl():
    def __init__(this):
        this.bowl = []

    def add_scoops(this, *args):
        this.bowl += [*args]

    def __repr__(this):
        return ", ".join(scoop.__repr__() for scoop in this.bowl)


def create_scoops() -> List[str]:
    return [
        Scoop('chocolate'),
        Scoop('vanilla'),
        Scoop('persimmon'),
    ]


if __name__ == "__main__":
    # print(create_scoops())
    s1, s2, s3 = Scoop('chocolate'), Scoop('vanilla'), Scoop('persimmon')
    b = Bowl()
    b.add_scoops(s1)
    b.add_scoops(s3, s2)
    print(b)
