from operator import itemgetter
from collections import namedtuple

Row = namedtuple("Row", ['first', 'last', 'time'])
PEOPLE = [
    Row('Donald', 'Trump', 7.85),
    Row('Vladimir', 'Putin', 3.626),
    Row('Jinping', 'Xi', 10.603)
]

template = "{1:10} {0:10} {2:.2f}"

if __name__ == '__main__':
    for row in sorted(PEOPLE, key=itemgetter(1,0)):
        print(template.format(*row))
    print("-------------------------------------")
    for row in sorted(PEOPLE, key=lambda row: (row.last, row.first)):
        print(f"{row.last:10} {row.first:10} {row.time:.2f}")
