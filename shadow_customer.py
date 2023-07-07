factor_cache = {}

def factorialMod(n, p):
    if n >= p:
        return 0

    result = 1
    for i in range(1, n + 1):
        result = (result * i) % p

    return result

def shadow_customer(inputs):
    for N, T in inputs:
        result = factor_cache.get((N, T))
        if not result:
            result = factorialMod(N, T)
            factor_cache[(N, T)] = result
        print(result)
    return result


if __name__ == '__main__':
    M = int(input())
    inputs = [map(int, input().split()) for _ in range(M+1)]
    shadow_customer(inputs)
