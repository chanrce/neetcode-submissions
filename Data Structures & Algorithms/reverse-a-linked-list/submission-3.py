# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First processed node becomes the last node,
        # so it should point to None.
        prev = None
        curr = head

        while curr:
            # Save where to go next before breaking the link.
            temp = curr.next

            # Reverse the arrow.
            curr.next = prev

            # This node is now the head of the reversed part.
            prev = curr

            # Move to the next node to process.
            curr = temp

        # prev now points to the new head.
        return prev