class MinHeap:
    def __init__(self):
        self.heap=[]
    def push(self,i):
        self.heap.append(i)
        j=len(self.heap)-1
        while j > 0:
            k = (j - 1) // 2

            if self.heap[k] < self.heap[j]:
                break

            self.heap[k], self.heap[j] = self.heap[j], self.heap[k]
            j = k

    def pop(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
        root=self.heap.pop()
        self.minHeapify(0)
        return root
    def minHeapify(self,i):
        while True:
            smallest=i
            left=2*i+1
            right=2*i+2
            if left<len(self.heap) and self.heap[left]<self.heap[smallest]:
                smallest=left
            if right<len(self.heap) and self.heap[right]<self.heap[smallest]:
                smallest=right
            if smallest==i:
                break
            self.heap[smallest],self.heap[i]=self.heap[i],self.heap[smallest]
            i=smallest



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap=MinHeap()
        vis=[0]*len(points)
        cost=0
        heap.push((0,0))
        while heap.heap:
            distance,node=heap.pop()
            if vis[node]:
                continue
            vis[node]=1
            cost+=distance
            x1,y1=points[node]
            for i in range(len(points)):
                if vis[i]:
                    continue
                x2,y2=points[i]
                distance = abs(x1 - x2) + abs(y1 - y2)
                heap.push((distance,i))
        return cost


                

        