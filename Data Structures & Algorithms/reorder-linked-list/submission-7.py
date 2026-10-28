# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find middle
        slow = head
        fast = head
        
        # fast lands on either: the last node or one step after it (None)
        # means we reached the end
        while fast and fast.next:
            #slow goes +1 steps
            slow = slow.next
            # fast goes +2 steps
            fast = fast.next.next

        # 2. Reverse second half
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 3. Interleave the two halves
        front = head
        back = prev

        while back:
            front_temp = front.next
            back_temp = back.next

            front.next = back
            back.next = front_temp

            front = front_temp
            back = back_temp