#!/bin/python3
import os

#
# Complete the 'findNumber' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#


def find_number(arr, k):
    if k in arr:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = []
    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)
    k = int(input().strip())
    result = find_number(arr, k)
    fptr.write(result + '\n')
    fptr.close()
