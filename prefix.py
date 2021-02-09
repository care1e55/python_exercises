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

if __name__ == "__main__":
    print(prefix_calc(input()))
