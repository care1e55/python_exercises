from itertools import cycle
from operator import add

step = 2
counter = 4
switch = cycle([(0, -1), (-1, 0), (0, 1), (1, 0)])


def init_matrix(n: int):
    if n % 2:
        center = n // 2
    else:
        center = n // 2 - 1
    matrix = [[0 for j in range(n)] for i in range(n)]
    matrix[center][center] = 1
    matrix[center][center + 1] = 2
    matrix[center + 1][center + 1] = 3
    return matrix, center + 1, center + 1


def print_matrix(matrix, pad):
    for i in matrix:
        print(' '.join(map(lambda x: f'{x:>{pad}}', i)).strip())


if __name__ == '__main__':
    n = int(input())
    max_counter = n**2
    matrix, current_i, current_j = init_matrix(n)
    for step in range(2, n + 1):
        for _ in range(2):
            case = next(switch)
            for i in range(step):
                if counter > max_counter:
                    break
                current_i, current_j = current_i + case[0], current_j + case[1]
                matrix[current_i][current_j] = counter
                counter += 1
    print_matrix(matrix, len(str(max_counter)))
