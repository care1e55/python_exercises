from collections import deque
from itertools import permutations
from random import choice, shuffle
import string
from copy import copy

SQUARE_SIZE = 26
initial = list(string.ascii_uppercase[:SQUARE_SIZE])
shuffle(initial)
triplet = deque(initial)
square = []

def print_square(square):
    for row in square:
        print(*row, sep="")        

for _ in range(SQUARE_SIZE):
    triplet.rotate()
    square.append(copy(triplet))

shuffle(square)
print_square(square)
