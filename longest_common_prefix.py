from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min(_str.__len__() for _str in strs)
        first_str = strs[0]
        prefix = []
        for i in range(min_length):
            if all(cur_str[i] == first_str[i] for cur_str in strs[1:]):
                prefix.append(first_str[i])
            else:
                return "".join(prefix)
        return "".join(prefix)
