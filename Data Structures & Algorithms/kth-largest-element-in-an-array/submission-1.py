class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap=[]
        for i in nums:
            self.push(i)
        for i in range(k-1):
            self.pop()
        return self.heap[0]


    def push(self,i)->None:
        self.heap.append(i)
        n=len(self.heap)-1
        while n>0:
            p=(n-1)//2
            if self.heap[p]>=self.heap[n]:
                break
            self.heap[p],self.heap[n]=self.heap[n],self.heap[p]
            n=p
    def pop(self)->None:
        largest=self.heap[0]
        p=self.heap.pop()
        if self.heap:
            self.heap[0]=p
            self.heapify_down(0)
        return largest
    def heapify_down(self,i)->None:
        while True:
            largest=i
            left=2*i+1
            right=2*i+2
            if left<len(self.heap) and self.heap[left]>self.heap[largest]:
                largest=left
            if right<len(self.heap) and self.heap[right]>self.heap[largest]:
                largest=right
            if largest==i:
                break
            self.heap[largest],self.heap[i]=self.heap[i],self.heap[largest]
            i=largest
        
        
        