buckets = [0 for _ in range(int(10e5))]
result = []

if __name__ == '__main__':
    N = int(input())
    prev = 0
    i = 1
    for a in map(int, input().split()):
        if a == 0:
            continue
        buckets[prev:a + 1 + prev] = [i for _ in range(a)]
        prev += a
        i += 1
    M = int(input())
    for p in map(int, input().split()):
        print(buckets[p-1])
