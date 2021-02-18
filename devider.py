if __name__ == '__main__':
    inuput_number = int(input())
    result = []
    for i in range(2, int(inuput_number**0.5) + 1):
        if not inuput_number % i:
            result += [i, inuput_number // i]
    print(*sorted(set(result)))
