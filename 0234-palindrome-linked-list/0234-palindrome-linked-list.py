# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        left, right = head, prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True