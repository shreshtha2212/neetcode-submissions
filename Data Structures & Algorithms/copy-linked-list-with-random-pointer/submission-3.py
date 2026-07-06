"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p=head
        
        while p:
            k=p.next
            v=Node(p.val)
            v.next=k
            p.next=v
            p=k
        p=head
        while p:
            if p.random:
                p.next.random=p.random.next
            else:
                p.next.random=None
            p=p.next.next
        if not head:
            return None
        p=head 
        copy=head.next
        tmp=copy
        while p:
            p.next=p.next.next
            if copy.next:
                copy.next=copy.next.next
            p=p.next
            copy=copy.next
        return tmp
        