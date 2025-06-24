# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return None
        lst = []
        current = head
        lst.append(current.val)
        while current.next:
            if current.next.val not in lst:
                lst.append(current.next.val)
                current = current.next
            else:
                current.next = current.next.next
        return head

