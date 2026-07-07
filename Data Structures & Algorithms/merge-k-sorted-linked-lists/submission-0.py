# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode(0)
        c=dummy
        heap=[]
        
        def heapify_up(i):
            heap.append(i)
            p=len(heap)-1
            while p>0:
                parent=(p-1)//2
                if heap[parent][0]<=heap[p][0]:
                    break
                heap[parent],heap[p]=heap[p],heap[parent]
                p=parent
        def delete():
            heap[0],heap[-1]=heap[-1],heap[0]
            return heap.pop()
        def heapify_down():
            idx=0
            
            while True:
                left=(2*idx)+1
                right=(2*idx)+2
                small=idx
                if left<len(heap) and heap[left][0]<heap[small][0]:
                    small=left
                if right<len(heap) and heap[right][0]<heap[small][0]:
                    small=right
                if small==idx:
                    break
                heap[idx],heap[small]=heap[small],heap[idx]
                idx=small

        for i in lists:
            if i:
                heapify_up((i.val,i))
        while heap:
            _,node=heap[0]
            c.next=heap[0][1]
            delete()
            if heap:
                heapify_down()
            if node.next:
                heapify_up((node.next.val,node.next))
            c=c.next
        return dummy.next



        




        