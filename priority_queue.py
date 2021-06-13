import heapq
import random
from string import ascii_lowercase


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Item({self.name})'

    def __str__(self):
        return f'Item({self.name})'


class PriorityQueue:
    def __init__(self):
        self.items = []
        self.index = 0

    def pop(self):
        return heapq.heappop(self.items)[-1]

    def push(self, item, priority):
        heapq.heappush(self.items, (priority, self.index, item))
        self.index += 1

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == '__main__':
    pq = PriorityQueue()
    [pq.push(Item(letter), random.randint(0, 10)) for letter in ascii_lowercase]
    print(pq)
    for _ in range(len(pq)):
        print(pq.pop())

