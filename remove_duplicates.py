from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                del nums[i]
                continue
            i += 1
        return len(nums)
        

if __name__ == '__main__':
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = s.removeDuplicates(nums)
    print(k)
    print(nums)
