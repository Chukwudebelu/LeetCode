# 328. Odd Even Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if (not head):
            return head
        else:
            odd_indices, even_indices = [], []
            curr1, curr2 = head, head
            ll_size = 0

            while (curr1):  # Get the number of nodes
                ll_size += 1
                curr1 = curr1.next

            count = 1   # Tracing index
            while (curr2 and (count <= ll_size)):
                if (count % 2 == 1):  # even numbered node
                    odd_indices += [ListNode(curr2.val)]
                elif (count % 2 == 0):  # odd numbered node
                    even_indices += [ListNode(curr2.val)]
                count += 1
                curr2 = curr2.next

            odd_indices.extend(even_indices)  # Merge odd & even numbered nodes

            for k in range(len(odd_indices)-1):
                odd_indices[k].next = odd_indices[k+1]                

            return odd_indices.pop(0)
