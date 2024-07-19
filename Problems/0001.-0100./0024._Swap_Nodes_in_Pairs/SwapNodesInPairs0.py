#!/bin/python3
# 24. Swap Nodes in Pairs

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Iterative approach
        curr = head
        length = 0
        l = []
        
        while (curr):
            l += [curr.val]
            curr = curr.next
            length += 1
            
        if (not head or length == 0): # empty linked list
            return head
        elif (length == 1): # 1-node in linked list
            return head
        else:    # 2-nodes or more in linked list
            if (length % 2 == 0): # even number of nodes
                for i in range(0, length, 2):
                    l[i], l[i+1] = l[i+1], l[i]  # swap
                    
            else:   # odd number of nodes
                for j in range(0, length-1, 2):
                    l[j], l[j+1] = l[j+1], l[j]  # swap
                    
            nodes = list(map(ListNode, l))
            
            for k in range(length-1):
                nodes[k].next = nodes[k+1]
                
            head_node = nodes.pop(0)
            
            return head_node
