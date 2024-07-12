#!/bin/python3
# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if (not list1 and not list2):
            return None
        elif (not list1):
            return list2
        elif (not list2):
            return list1
        else:
            l1, l2 = [], []
            curr1, curr2 = list1, list2

            while (curr1):
                l1 += [curr1.val]
                curr1 = curr1.next

            while (curr2):
                l2 += [curr2.val]
                curr2 = curr2.next

            _list_ = [*map(ListNode, sorted(l1 + l2))]

            for i in range(0, len(_list_)-1):
                _list_[i].next = _list_[i+1]

            return _list_[0]
