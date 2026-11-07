# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #set left and right pointers
        dummy=ListNode(0)
        dummy.next=head
        l=dummy
        r=head
        #go thru whole list until r reaches end
        #make distance between l and r=n+1 distance
        while n>0:
            r=r.next
            n-=1
        while r:
            #move r pointer forward til reaches end
            l=l.next
            r=r.next
        #make left pointer point to the next next node
        l.next=l.next.next
        
        return dummy.next
        
        
            
        