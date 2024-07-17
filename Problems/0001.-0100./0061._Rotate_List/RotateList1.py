#!/bin/python3
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (head is None):    # empty linked list
            return head
        elif (head is not None and k == 0):    # No rotations!
            return head
        else:
            size = 0
            node_data = []

            while (head):
                node_data += [head.val]
                head = head.next
                size += 1

            k = pow(k, 1, size)  # k (mod size)

            post_nodes = node_data[0:size-k]
            pre_nodes = node_data[size-k:]
            rotated_nodes_data = pre_nodes + post_nodes
            rotated_nodes = [*map(ListNode, rotated_nodes_data)]

            for l in range(0, size-1, 1):
                rotated_nodes[l].next = rotated_nodes[l+1]

            rotated_head = rotated_nodes.pop(-size)
            return rotated_head
