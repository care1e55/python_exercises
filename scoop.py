from typing import List

class Scoop():
    def __init__(this, flavor: str = None):
        this.flavor = flavor

    def __repr__(this) -> str:
        return this.flavor

def create_scoops() -> List[str]:
    return [
        Scoop('chocolate'),
        Scoop('vanilla'),
        Scoop('persimmon'),
    ]

if __name__ == "__main__":
    print(create_scoops())
