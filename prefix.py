from operator import add, sub, mul, truediv, mod, pow

dispach_oeprator = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv,
    "%": mod,
    "**": pow
}

def prefix_calc(expresion: str):
    op, first, second = expresion.split()
    return dispach_oeprator[op](int(first), int(second))

def prefix_calc_args(expresion: str):
    op, args = expresion.split()[0], expresion.split()[1:] 
    result = 0
    for arg in args:
        result = dispach_oeprator[op](result, int(arg))
    return result


if __name__ == "__main__":
    # print(prefix_calc(input()))
    print(prefix_calc_args(input()))
