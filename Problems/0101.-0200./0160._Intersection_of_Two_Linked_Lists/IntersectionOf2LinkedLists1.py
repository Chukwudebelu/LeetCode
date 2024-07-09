# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Hashtable for the Linked Lists: ID of head & values
        nodes = dict()
        
        while (headA is not None):
            nodes[id(headA)] = headA.val
            headA = headA.next
            
        # Check for node with the same thing in Linked List B
        while (headB):
            if id(headB) in nodes:
                return headB
            headB = headB. next
