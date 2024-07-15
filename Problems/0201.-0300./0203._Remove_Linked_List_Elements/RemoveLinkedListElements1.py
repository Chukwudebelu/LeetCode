#!/bin/python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if (not head):  # empty linked list
            return head
        else:
            length = 0
            curr = head
            _list_ = []
            
            while (curr):   # Count number of nodes
                length += 1
                _list_.append(curr.val)
                curr = curr.next

            re = 0
            while (0 <= re < length):
                if (_list_[re] == val):
                    del _list_[re]   # remove element
                    re -= 1          # Shift pointer left
                    length -= 1      # reduce size of linked list
                re += 1

            final_linked_list = list(map(ListNode, _list_))

            for i in range(len(final_linked_list)-1):
                final_linked_list[i].next = final_linked_list[i+1]

            new_head = final_linked_list[0] if (len(final_linked_list) != 0) else None
            return new_head
