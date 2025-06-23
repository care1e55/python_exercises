from copy import copy
from itertools import zip_longest
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, _list: list):
        next = ListNode(_list[-1], None)
        for val in _list[-2::-1]:
            current = ListNode(val, next)
            next = current
        return current


class Solution:
    def mergeTwoLists(
        self, 
        list1: Optional[ListNode], 
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        for i1, i2 in zip_longest(list1, list2):
            raise NotImplementedError
            

if __name__ == '__main__':
    list1 = ListNode.from_list([1,2,4])
    list2 = ListNode.from_list([1,3,4])
    output = ListNode.from_list([1,1,2,3,4,4])
    assert Solution().mergeTwoLists(list1, list2) == output

    list1 = ListNode.from_list([])
    list2 = ListNode.from_list([])
    output= ListNode.from_list([])
    assert Solution().mergeTwoLists(list1, list2) == output

    list1 = ListNode.from_list([])
    list2 = ListNode.from_list([0])
    output= ListNode.from_list([0])
    assert Solution().mergeTwoLists(list1, list2) == output

