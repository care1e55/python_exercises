from typing import List, Optional
import random


def generate_random(length: int = 10, limit: int = 100) -> List[int]:
    "generate random int list sequence"
    return [random.randint(0, limit) for _ in range(length)]


def recursive_binary_search(sequence, target, low, high):
    mid = (high - low) // 2
    if target == sequence[mid]:
        return mid
    elif low >= high:
        return None
    if target > sequence[mid]:
        return recursive_binary_search(sequence, target, mid, high)
    elif target < sequence[mid]:
        return recursive_binary_search(sequence, target, low, mid)


def iterative_binary_search(sequence, target) -> Optional[int]:
    pass


binary_search = {
    "iterative": iterative_binary_search,
    "recursive": recursive_binary_search
}


def search(sequence, target, how='recursive') -> Optional[int]:
    "perform iterative or recursive search"
    return binary_search[how](sequence, target, 0, len(sequence))


if __name__ == '__main__':
    sequence = sorted(generate_random())
    result = search(sequence, sequence[3])
    print(sequence)
    print(result)
