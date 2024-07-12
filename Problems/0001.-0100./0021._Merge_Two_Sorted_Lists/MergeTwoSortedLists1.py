#!/bin/python3

import sys
sys.setrecursionlimit(100)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if (list1 is None and list2 is None):   return None
        elif (list1 is None):   return list2
        elif (list2 is None):   return list1
        else:
            if (list2.val > list1.val):
                return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
            else:   # (list1.val > list2.val)
                return ListNode(list2.val, self.mergeTwoLists(list2.next, list1))
