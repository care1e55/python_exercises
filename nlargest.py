
if __name__ == '__main__':
    _, n = input().split()
    array = list(map(int, input().split()))
    result = sorted(set(array), reverse=True)[int(n)-1]
    print(result)
