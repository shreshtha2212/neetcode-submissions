# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        j=ListNode()
        k=j
        j.val=0
        j.next=None
        while list1 and list2:
            if list1.val<=list2.val:
                j.next=list1
                list1=list1.next
                j=j.next
            elif list2.val<list1.val:
                j.next=list2
                list2=list2.next
                j=j.next
        if list1:
            j.next=list1
        elif list2:
            j.next=list2
        return k.next

        