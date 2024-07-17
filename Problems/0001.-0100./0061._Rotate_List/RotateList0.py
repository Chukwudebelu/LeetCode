#!/bin/python3
# 61. Rotate List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if (not head):    # empty linked list
            return None
        elif (head and k == 0):    # No rotations!
            return head
        else:
            curr = head
            length = 0
            node_vals = list()

            while (curr):
                node_vals.append(ListNode(curr.val))
                length += 1
                curr = curr.next

            k %= length    # get smallest amount of rotations for same results

            new = []
            for i in range(k):
                new = [node_vals.pop(-1)] + new

            new += node_vals
            for j in range(length-1):
                new[j].next = new[j+1]

            return new[0]
