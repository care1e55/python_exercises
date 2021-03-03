import math
import operator

SIZE = 4
SQRT = int(math.sqrt(SIZE))


def get_column(list_, n):
    return map(operator.itemgetter(n), list_)


def get_input_field():
    return [[int(i) for i in input()] for _ in range(SIZE)]


def is_valid(num, row, column, field):
    "check whether we can put that number"
    # check row
    if num in field[row]:
        return False
    # check column
    if num in get_column(field, column):
        return False
    # check square
    start_row = row - row % SQRT
    start_column = column - column % SQRT
    for i in range(SQRT):
        for j in range(SQRT):
            if field[i + start_row][j + start_column] == num:
                return False
    return True


def solve(row, column, field):
    "iterate over and solve"
    if row == SIZE-1 and column == SIZE:
        return True
    # next row   
    if column == SIZE:
        column = 0
        row += 1
    # already have number
    if field[row][column]:
        return solve(row, column+1, field)
    # try put number
    for num in range(1, SIZE+1):
        if is_valid(num, row, column, field):
            field[row][column] = num
            if solve(row, column+1, field):
                return True
        field[row][column] = 0
    return False


def print_field(field):
    for row in field:
        print(*row, sep="")


if __name__=="__main__":
    field = get_input_field()
    if solve(0, 0, field):
        print_field(field)
