#!/bin/python3
#
# 160. Intersection of Two Linked Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA, currB = headA, headB
        sizeA, sizeB = 0, 0
        
        while (currA):
            sizeA += 1
            currA = currA.next
            
        while (currB):
            sizeB += 1
            currB = currB.next
            
        if (sizeA > sizeB): # LinkedListA has (sizeA - sizeB) more elements than LinkedListB
            for _ in range(sizeA - sizeB):
                headA = headA.next
                
            while (headA and headB):
                if (headA is headB and headA.val == headB.val):
                    return headA
                headA = headA.next
                headB = headB.next
        
        elif (sizeA < sizeB): # LinkedListB has (sizeB - sizeA) more elements than LinkedListA
            for _ in range(sizeB - sizeA):
                headB = headB.next
            
            while (headA and headB):
                if (headA is headB and headA.val == headB.val):
                    return headB
                headA = headA.next
                headB = headB.next
            
        elif (sizeA == sizeB): # LinkedListA is LinkedListB            
            while (headA and headB):
                if (headA is headB):
                    return headA                
                headA = headA.next
                headB = headB.next

            return None # No intersection
