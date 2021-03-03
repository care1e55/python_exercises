import math
SIZE = 4
SQRT = int(math.sqrt(SIZE))

test_field = [
    [1,2,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,2,4],
]


def get_input_field():
    return [[i for i in input()] for _ in range(4)]


def is_valid(num, row, column, field):
    "check whether we can put that number"
    # check row
    if num in field[row]:
        return False
    # check column
    if num in field[:][column]:
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
    print(field)
    if row == SIZE-1 and col == SIZE:
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


if __name__=="__main__":
    if solve(0, 0, test_field):
        print(test_field)
