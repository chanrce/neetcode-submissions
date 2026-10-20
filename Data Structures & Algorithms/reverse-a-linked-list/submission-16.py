# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # BASE CASE
        if not head or not head.next:
            return head

        # RECURSIVE CASE
        newHead = self.reverseList(head.next)

        # REVERSE THE CONNECTION
        head.next.next = head
        head.next = None

        # RETURN
        return newHead