#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'powerJump' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING game as parameter.
#


def powerJump(game):
    from itertools import groupby
    last_step = game[-1]
    max_power = 1
    for k, g in groupby(game):
        print(k, (list(g)))
        if k != last_step:
            power = len(list(g))
            if power >= max_power:
                max_power = power + 1
    return max_power

# def powerJump(game):
#     last_step = game[-1]
#     prev_step = game[0]
#     max_power = 0
#     power_counter = 1
#     for cell in game[1:]:
#         print(cell, power_counter, max_power)
#         if cell != last_step:
#             if cell != prev_step:
#                 max_power = power_counter
#                 power_counter = 1
#         else:
#             power_counter += 1
#     return max_power + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    game = input()

    result = powerJump(game)

    fptr.write(str(result) + '\n')

    fptr.close()
