if __name__ == '__main__':
    buffer = []
    with open("input.txt") as file:
        buffer = file.readlines()
    for i, line in enumerate(buffer, 1):
        print(f'{i:>4} {line}', end='')
