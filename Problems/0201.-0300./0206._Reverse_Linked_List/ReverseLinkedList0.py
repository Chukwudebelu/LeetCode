#!/bin/python3
# 206. Reverse Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if (head is None):    # Empty Linked List: _ -> NULL
            return None
        elif (head.next is None):    # Unary Linked List: x -> NULL
            return head
        else:    # Binary Linked List & others: x -> y -> NULL
            curr = head
            prev = None
            
            while (curr):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
