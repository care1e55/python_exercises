from collections import deque
from itertools import permutations
from random import choice

triplet = deque(choice(list(permutations("ABC"))))
for _ in range(3):
    triplet.rotate()
    print(*triplet, sep="")


# for i in permutations(inital):
#     print(i)
