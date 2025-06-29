from copy import copy, deepcopy
from itertools import zip_longest
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, _list: list):
        if not _list:
            return None
        next = ListNode(_list[-1], None)
        if len(_list) == 1:
            return next 
        for val in _list[-2::-1]:
            current = ListNode(val, next)
            next = current
        return current
    
    def __str__(self):
        return f'val={self.val} next={self.next.val if self.next else 'None'}'


class Solution:
    def mergeTwoLists(
        self, 
        list1: Optional[ListNode], 
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        _list1 = deepcopy(list1)
        _list2 = deepcopy(list2)

        # handle first
        if _list1.val <= _list2.val:
            current_node = ListNode(val=_list1.val)
            _list1 = _list1.next
        else:
            current_node = ListNode(val=_list2.val)
            _list2 = _list2.next
        root = current_node

        if _list2 is None:
            current_node.next = ListNode(val=_list1.val)
            return root
        if _list1 is None:
            current_node.next = ListNode(val=_list2.val)
            return root
        

        while _list1.next and _list2.next:
            if _list1.val <= _list2.val:
                current_node.next = ListNode(_list1.val)
                _list1 = _list1.next
            else:
                current_node.next = ListNode(_list2.val)
                _list2 = _list2.next
            current_node = current_node.next

        if _list2 is None:
            current_node.next = _list1
            return root
        if _list2 is None:
            current_node.next = _list2
            return root


        # handle last
        if _list1.val <= _list2.val:
            current_node.next = ListNode(val=_list1.val)
            current_node = current_node.next
            current_node.next = ListNode(val=_list2.val)
        else:
            current_node.next = ListNode(val=_list2.val)
            current_node = current_node.next
            current_node.next = ListNode(val=_list1.val)
        return root

        
            

if __name__ == '__main__':
    # list1 = ListNode.from_list([1,2,4])
    # list2 = ListNode.from_list([1,3,4])
    # output = ListNode.from_list([1,1,2,3,4,4])

    list1 = ListNode.from_list([-9,3])
    list2 = ListNode.from_list([5,7])

    result = Solution().mergeTwoLists(list1, list2)
    print(result)
    print(result.next)
    print(result.next.next)
    print(result.next.next.next)
    # assert result == output

    list1 = ListNode.from_list([])
    list2 = ListNode.from_list([])
    output= ListNode.from_list([])
    # assert Solution().mergeTwoLists(list1, list2) == output

    list1 = ListNode.from_list([])
    list2 = ListNode.from_list([0])
    output= ListNode.from_list([0])
    # assert Solution().mergeTwoLists(list1, list2) == output

