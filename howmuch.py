if __name__ == '__main__':
    large_num = reversed(input())
    result = [
        digit if pos % 3 else " " + digit
        for pos, digit in enumerate(large_num, 1)
    ]
    print("".join(reversed(result)).strip())
