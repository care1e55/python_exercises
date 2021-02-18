if __name__ == '__main__':
    even, odd = [], []
    for pos, number in enumerate(input(), 1):
        if pos % 2:  # odd
            odd.append(int(number))
        else:  # even
            even.append(int(number))
    if not (sum(odd) + 3*sum(even)) % 10:
        print('yes')
    else:
        print('no')
