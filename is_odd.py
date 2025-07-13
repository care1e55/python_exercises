from typing import List


def is_odd(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i != j:
                if (nums[i]*nums[j]) % 2:
                    return False
    return True

if __name__ == '__main__':
    assert is_odd([1, 2, 2, 2]) == True
    assert is_odd([3, 1, 2, 2]) == False
