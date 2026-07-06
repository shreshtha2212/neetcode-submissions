# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        k=l1
        m=l2
        carry=0
        dummy=ListNode(0)
        dummy.next=None
        j=dummy
        while m or k:
            x=k.val if k else 0
            y=m.val if m else 0
            s=x+y+carry
            p=s%10
            carry=s//10
            i=ListNode(p)
            j.next=i
            j=j.next
            if m:
                m=m.next
            if k:
                k=k.next
        if carry:
            j.next=ListNode(carry)
        return dummy.next
            
        



        