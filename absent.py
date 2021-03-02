from typing import List


def find_missing(sequence: List[str]):
    etalon = "123456789"
    sequence.sort()
    for i in range(len(sequence)):
        if etalon[i] != sequence[i]:
            return i+1
    return None

if __name__ == "__main__":
    print(find_missing(list(input())))
