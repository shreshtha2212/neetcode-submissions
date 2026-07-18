class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=[]
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        self.push(val)
        if len(self.heap)>self.k:
          self.pop()
        return self.heap[0]


    def push(self,val:int)->None:
        self.heap.append(val)
        i=len(self.heap)-1
        
        while i>0:
            p=(i-1)//2
            if self.heap[p]<=self.heap[i]:
                break
            self.heap[p],self.heap[i]=self.heap[i],self.heap[p]
            i=p
    def pop(self)->int:
        smallest=self.heap[0]
        last=self.heap.pop()
        if self.heap:
            self.heap[0]=last
            self.heapify_down(0)
        return smallest
    def heapify_down(self, index: int)->None:
        size=len(self.heap)
        while True:
            left=2*index+1
            right=2*index+2
            smallest=index
            if left<size and self.heap[left]<self.heap[smallest]:
                smallest=left
            if right<size and self.heap[right]<self.heap[smallest]:
                smallest=right
            if smallest==index:
                break
            self.heap[index], self.heap[smallest]=self.heap[smallest], self.heap[index]
            index=smallest



        
