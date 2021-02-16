if __name__ == '__main__':
    result = 0
    with open("input.txt") as file:
        for i, line in enumerate(file.readlines(), 1):
            if not i % 2:
                result += int(line)
    print(result)
