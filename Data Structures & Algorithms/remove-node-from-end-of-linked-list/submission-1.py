# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rev(l):
            g=None
            j=l
            while j:
                p=j.next
                j.next=g
                g=j
                j=p
            return g
        h=rev(head)
        p=h
        if n==1:
            h=h.next
            return rev(h)
        cnt=0
        while h:
            cnt+=1

            if cnt==n-1:
                h.next=h.next.next
                break
            h=h.next
        return rev(p)
            

        