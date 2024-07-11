#!/bin/python3
# Definition for singly-linked list.
# Code works but gives Time Limit Exceeded (TLE) error for huge linked lists with ~ 10⁵ nodes

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        forward_nodes, backward_nodes = [], []
        
        while (head != None):
            forward_nodes += [head.val]
            backward_nodes = [head.val] + backward_nodes
            head = head.next

        if (forward_nodes == backward_nodes):
            return True
        else:
            return False
