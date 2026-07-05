# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def rev(p):
            k=None
            j=p
            while j:
                y=j.next
                j.next=k
                k=j
                j=y
            return k
        u=head      
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        t=rev(second)
        while t:
            tmp1=u.next
            tmp2=t.next
            u.next=t
            t.next=tmp1
            u=tmp1
            t=tmp2
        
        



        
        