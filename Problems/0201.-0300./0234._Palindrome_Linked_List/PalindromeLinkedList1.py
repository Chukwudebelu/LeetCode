#!/bin/python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head: ListNode) -> bool:
        nodesData = list()
        
        while (head is not None):
            nodesData.append(head.val)
            head = head.next
            
        return 1 if ([*reversed(nodesData)] == nodesData) else 0
