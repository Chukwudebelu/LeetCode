#!/bin/python3
# 234. Palindrome Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head: ListNode) -> bool:
        llist = []
        curr = head
        
        while (curr):
            llist += [curr.val]
            curr = curr.next
            
        return (llist == llist[::-1])
