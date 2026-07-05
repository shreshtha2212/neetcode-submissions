# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f=None
        j=head
        while j:
            p=j.next
            j.next=f
            f=j
            j=p
        return f
            
        