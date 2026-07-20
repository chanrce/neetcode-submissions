# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        # Put values into array
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        # Reverse array
        arr.reverse()

        # Empty list?
        if not arr:
            return None

        # Create head of new linked list
        head = ListNode(arr[0])
        curr = head

        # Add remaining nodes
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next

        return head