#!/bin/python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if (not head or k == 0):
            return head
            
        # Get number of nodes in the linked list
        curr1 = head
        length = 0
        while (curr1):  
            curr1 = curr1.next
            length += 1
            
        if (k == length):   # rotate back to original
            return head

        k %= length
        if (k == 0):    # No rotation
            return head
        
        # (0 < k < length)        
        i = 0   # node position
        while (i < length-k-1):
            lead = lead.next
            i += 1
        
        lead2 = lead.next
        lead.next = None
        
        if (length == 1): return head    # 1 node in the linked list

        tail = lead2
        while (tail.next):
            tail = tail.next
            
        tail.next = head
        return lead2
