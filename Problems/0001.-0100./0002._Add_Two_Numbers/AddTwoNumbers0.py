#!/bin/python3
# 2. Add Two Numbers

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
      
class Solution:
    # def List2Num(self, l: list) -> int:
    #         number = 0
    #         for i in range(0, len(l), +1):
    #             number += (10**i)*l[i]
    #         return number
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Edge case: Both linked lists have a single node with value of 0
        if (l1.val == 0 and l2.val == 0 and l1.next is None and l2.next is None):
            return l1
        else:
            curr1, curr2 = l1, l2
            num1 = []
            while (curr1):
                num1 = [curr1.val] + num1  # Hold linked list 1 node values in reverse
                curr1 = curr1.next

            num2 = []
            while (curr2):
                num2 = [curr2.val] + num2  # Hold linked list 2 node values in reverse
                curr2 = curr2.next

            n1 = int(''.join(map(str, num1)))  # n1 = self.reverseList2Num(num1)      
            n2 = int(''.join(map(str, num2)))  # n2 = self.reverseList2Num(num2)
            n = n1 + n2
            final_list = []

            while (n):
                final_list.append(ListNode(n % 10))
                n //= 10

            for i in range(len(final_list)-1):
                final_list[i].next = final_list[i+1]

            return final_list[0]
