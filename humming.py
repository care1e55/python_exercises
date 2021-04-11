import sys


def hamming_distance(first: str, second: str) -> int:
    """
    Computes and returns humming distance of the two strings.
    More on that: https://en.wikipedia.org/wiki/Hamming_distance

            Parameters:
                    first (str): first string
                    second (str): second string

            Returns:
                    score (int): humming distanse
    """
    score = 0
    for i in range(min(len(first), len(second))):
        if first[i] != second[i]:
            score += 1
    return score


def hamming_distance_short(first: str, second: str) -> int:
    """
    Short version of humming distance
    More on that: https://en.wikipedia.org/wiki/Hamming_distance

            Parameters:
                    first (str): first string
                    second (str): second string

            Returns:
                    score (int): humming distanse
    """

    if len(first) != len(second):
        print('Must be equal size')
        return None
    return sum(x != y for x, y in zip(first, second))


def main(first: str, second: str):
    hamming_distance(first, second)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
