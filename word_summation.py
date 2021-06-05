import sys
from string import ascii_lowercase


class Solution:

    def __init__(self):
        self.alphanum_mapping = {c: str(i) for i, c in enumerate(ascii_lowercase)}

    def is_sum_equal(self, *args) -> bool:
        fist_num, second_num, target_num = tuple(map(self._word_num, args))
        return (fist_num + second_num) == target_num

    def _word_num(self, word: str) -> int:
        return int("".join(list(map(lambda c: self.alphanum_mapping[c], word))))


if __name__ == '__main__':
    result = Solution.isSumEqual(sys.argv[1:4])
    print(result)
