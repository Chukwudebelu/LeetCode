#!/bin/python3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Edge case: Both linked lists have a single node with value of 0
        if (l1.val == 0 and l2.val == 0 and l1.next is None and l2.next is None):
            return l1
        else:
            curr1, curr2 = l1, l2
            number1, i = 0, 0
            
            while (curr1):
                number1 += (curr1.val)*(10**i)  # Convert linked list 1 node values to an integer
                i += 1
                curr1 = curr1.next

            number2, j = 0, 0
            while (curr2):
                number2 += (curr2.val)*(10**j)  # Convert linked list 2 node values to an integer
                j += 1
                curr2 = curr2.next

            number = number1 + number2
            l3 = list()

            while (number):
                l3 += [ListNode(number % 10)]   # Create a Node object with the last digit
                number //= 10   # Remove the last digit

            for i in range(len(l3)-1):
                l3[i].next = l3[i+1]
                
            head_node = l3.pop(0)    # Get the head of the new singly linked list
            
            return head_node
