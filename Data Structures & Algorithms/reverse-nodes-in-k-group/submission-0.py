# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        groupPrev=dummy
        def kth(i):
            cnt=0
            while i and cnt!=k:
                i=i.next
                cnt+=1
            return i
        while True:
            h=kth(groupPrev)
            if not h:
                break
            groupNxt= h.next
            prev=h.next
            cur=groupPrev.next
            while cur!=groupNxt:
                tmp=cur.next
                cur.next=prev
                prev=cur
                cur=tmp
            n=groupPrev.next
            groupPrev.next=h
            groupPrev=n

        return dummy.next

            
        