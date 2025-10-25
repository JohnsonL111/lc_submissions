# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        
        ptrA = headA
        ptrB = headB
        # a = length of non shared for A
        # b = length of non shared for B
        # c = length of shared between A and B
        while ptrA != ptrB:
            if ptrA:
                ptrA = ptrA.next
            else:
                ptrA = headB
            
            if ptrB:
                ptrB = ptrB.next
            else:
                ptrB = headA
        
        return ptrA


        