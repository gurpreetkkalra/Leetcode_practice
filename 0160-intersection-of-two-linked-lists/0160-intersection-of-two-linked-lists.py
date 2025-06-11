# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA and not headB:
            return None
        
        ptrA = headA
        ptrB = headB

        while ptrA != ptrB:
            if ptrA is None:
                ptrA = headB
            else:
                ptrA = ptrA.next

            if ptrB is None:
                ptrB = headA
            else:
                ptrB = ptrB.next
            
        return ptrB
            
            

