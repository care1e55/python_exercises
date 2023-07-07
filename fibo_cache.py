import time

cache_table = {}


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Time: {end - start} seconds')
        return result

    return wrapper


def cache(func):
    def wrapper(*args, **kwargs):
        number = args[0]
        if cache_table.get(number):
            return cache_table[number]
        else:
            cache_table[number] = func(number)
            return cache_table[number]

    return wrapper


def fibonacci_iter(number: int):
    """P[n] = P[n-1] + P[n-1]"""
    p1 = 1
    p2 = 2
    for i in range(2, number):
        p3 = p1 + p2
        p1 = p2
        p2 = p3
    return p3


@measure_time
def fibonacci_recur(number: int):
    @cache
    def fibonacci_wrapper(number: int):
        """P[n] = P[n-1] + P[n-2]"""
        if number == 1:
            return 1
        if number == 2:
            return 2
        return fibonacci_wrapper(number - 1) + fibonacci_wrapper(number - 2)

    return fibonacci_wrapper(number)


if __name__ == '__main__':
    print(fibonacci_iter(36))
    print(fibonacci_recur(36))
