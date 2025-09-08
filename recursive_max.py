from enum import Enum
from typing import List


class RecursiveType(Enum):
    MIN = 'min'
    MAX = 'max'


def find_recursive(sequence: List, recursive_type: RecursiveType):
    return _find_recursive(-1, sequence, recursive_type) 
    

def _find_recursive(current_n: int, sequence: List, recursive_type: RecursiveType):
    current_n += 1
    if current_n == len(sequence)-1:
        return sequence[current_n]
    prev = _find_recursive(current_n, sequence, recursive_type)
    match recursive_type:
        case RecursiveType.MAX:
            if sequence[current_n] > prev:
                return sequence[current_n]
            return prev
        case RecursiveType.MIN:
            if sequence[current_n] < prev:
                return sequence[current_n]
            return prev


if __name__ == "__main__":
    test_sequence = [1, 1, 3, 6, 2]
    expected_result = 6
    result = find_recursive(test_sequence, RecursiveType.MAX)
    assert result == expected_result

    expected_result = 1
    result = find_recursive(test_sequence, RecursiveType.MIN)
    assert result == expected_result


    test_sequence = [2, 7, 3, 6, 2, 4, 54, 423, 4, 4, 4]
    expected_result = 423
    result = find_recursive(test_sequence, RecursiveType.MAX)
    assert result == expected_result

    expected_result = 2
    result = find_recursive(test_sequence, RecursiveType.MIN)
    assert result == expected_result

