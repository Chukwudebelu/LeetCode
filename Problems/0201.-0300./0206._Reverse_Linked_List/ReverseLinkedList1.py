#!/bin/python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode]) -> ListNode:
        if (head is None or not head.next):
            return head
        else:
            llist = list()
            curr = head

            while (curr is not None):
                llist = [curr.val] + llist  # Store the node values in reverse
                curr = curr.next

            nodes = [*map(ListNode, llist)]  # Create node objects from the values

            for i in range(len(llist)-1):  # Link the node objects to create the singly linked list
                nodes[i].next = nodes[i+1]

            headNode = nodes.pop(0)
            return (headNode)
