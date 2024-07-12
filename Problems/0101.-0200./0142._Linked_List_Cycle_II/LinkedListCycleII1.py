#!/bin/python3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if (not head):  # Empty Linked List has no cycle
            return None
        else:
            nodes = set()  # More efficient than using a list
            
            while (head is not None):                
                if (head in nodes):
                    return head
                nodes.add(head)
                head = head.next
