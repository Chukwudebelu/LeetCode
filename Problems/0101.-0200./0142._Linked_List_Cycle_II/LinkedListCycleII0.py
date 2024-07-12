#!/bin/python3
# 142. Linked List Cycle II

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if (not head):    # Empty Linked List has no cycle
            return None
        else:
            linkedListNodes = list()
            
            while (head):                
                if (head not in linkedListNodes):
                    linkedListNodes.append(head)
                else:
                    break
                head = head.next
                
            ans = [node for node in linkedListNodes if (node == head)]
            return ans[0] if (len(ans) != 0) else None
