# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        length = 0
        current = head
        while current:
            length+=1
            current = current.next
        mid = length // 2
        current = head
        i = 0
        while i < mid:
            current = current.next
            i += 1
        return current

