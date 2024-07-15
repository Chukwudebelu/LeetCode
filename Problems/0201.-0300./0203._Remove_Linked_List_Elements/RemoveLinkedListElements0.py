#!/bin/python3
# 203. Remove Linked List Elements

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ll_size = 0
        curr = head

        while (curr):  # Count the number of nodes in the Singly Linked List
            ll_size += 1
            curr = curr.next
        
        if (not head and ll_size == 0):  # Empty Linked List
            return head
        elif (ll_size == 1):  # Linked List with 1 node
            if (head.val == val):
                return None
            else:
                return head
        else:   # Linked List with 2 or more nodes
            dummy = ListNode(-1, head) # dummy.next = head
            prev = dummy
            
            while (head):
                if (head.val == val):
                    prev.next = head.next
                else:
                    prev = head
                    
                head = head.next
            return dummy.next
