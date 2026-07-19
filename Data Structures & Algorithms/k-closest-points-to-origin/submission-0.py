class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap=[]
        for i in points:
            x=i[0]
            y=i[1]
            d=x*x+y*y
            self.push((d,i))
        res=[]
        for i in range(k):
            dis,point=self.pop()
            res.append(point)
        return res




    def push(self,i)->None:
        self.heap.append(i)
        j=len(self.heap)-1
        while j>0:
            p=(j-1)//2
            if self.heap[p][0]<=self.heap[j][0]:
                break
            self.heap[p],self.heap[j]=self.heap[j],self.heap[p]
            j=p
    def pop(self)->int:
        smallest=self.heap[0]
        k=self.heap.pop()
        if self.heap:
            self.heap[0]=k
            self.heapify_down(0)
        return smallest
    def heapify_down(self,i):
        while True:
            smallest=i
            left=2*i+1
            right=2*i+2
            if left<len(self.heap) and self.heap[left][0]<self.heap[smallest][0]:
                smallest=left
            if right<len(self.heap) and self.heap[right][0]<self.heap[smallest][0]:
                smallest=right
            if smallest==i:
                break
            self.heap[smallest],self.heap[i]=self.heap[i],self.heap[smallest]
            i=smallest

            
        