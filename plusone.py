
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = "".join(str(digit) for digit in digits)
        digits_int = int(digits_str) + 1
        return [int(digit) for digit in str(digits_int)]


if __name__ == "__main__":
    s = Solution()
    test_digits_1 = [1,2,3]
    test_result_1 = [1,2,4]
    assert s.plusOne(test_digits_1) == test_result_1
    test_digits_2 = [4,3,2,1]
    test_result_2 = [4,3,2,2]
    assert s.plusOne(test_digits_2) == test_result_2
    test_digits_3 = [9]
    test_result_3 = [1,0]
    assert s.plusOne(test_digits_3) == test_result_3
    
    print("Solution is OK")
