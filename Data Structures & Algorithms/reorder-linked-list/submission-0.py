# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        q = deque()
        node = head.next
        
        while node:
            q.append(node)
            node = node.next
        
        node = head
        
        while q:
            temp = q.pop()
            node.next = temp
            node = node.next
            
            if q:
                temp = q.popleft()
                node.next = temp
                node = node.next
        
        node.next = None