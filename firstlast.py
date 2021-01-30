from typing import Sequence

def firstlast(sequence: Sequence) -> Sequence:
    return sequence[:1] + sequence[-1:]

if __name__ == '__main__':
    examples = [
        [1,2,3,4],
        ["1", "2", "3"],
        ('kek', "lol", "kek"),
        "hmmmmmm"
        ]
    for example in examples:
        print(firstlast(example))
