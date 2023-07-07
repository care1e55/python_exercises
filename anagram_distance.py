#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinimumDifference' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY a
#  2. STRING_ARRAY b
#

def getMinimumDifference(a, b):
    result = []
    for first, second in zip(a, b):
        # print(first, second)
        if len(first) != len(second):
            result.append(-1)
            continue
        answer = 0
        first, second = sorted(list(first)), sorted(list(second))
        while True:
            # print(first, second)
            if len(first) == 0 or len(second) == 0:
                answer += len(first) + len(second)
                break
            if first[-1] > second[-1]:
                answer += 1
                first.pop()
            elif first[-1] < second[-1]:
                answer += 1
                second.pop()
            else:
                first.pop()
                second.pop()
        result.append(answer//2)
    return result






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = input()
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = input()
        b.append(b_item)

    result = getMinimumDifference(a, b)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
