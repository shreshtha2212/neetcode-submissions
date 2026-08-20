class MinHeap:
    def __init__(self):
        self.minHeap=[]
    def push(self,i):
        self.minHeap.append(i)
        k=len(self.minHeap)-1
        while k>0:
            p=(k-1)//2
            if self.minHeap[p]<self.minHeap[k]:
                break
            self.minHeap[p],self.minHeap[k]=self.minHeap[k],self.minHeap[p]
            k=p
    def pop(self):
        if len(self.minHeap)==0:
            return None
        if len(self.minHeap)==1:
            return self.minHeap.pop()
        root=self.minHeap[0]
        self.minHeap[0]=self.minHeap.pop()
        self.minHeapify(0)
        return root
    def minHeapify(self,i):
        while True:
            smallest=i
        
            left=2*i+1
            right=2*i+2
            if left<len(self.minHeap) and self.minHeap[left]<self.minHeap[smallest]:
                smallest=left
            if right<len(self.minHeap) and self.minHeap[right]<self.minHeap[smallest]:
                smallest=right
            if i==smallest:
                break
            self.minHeap[smallest],self.minHeap[i]=self.minHeap[i],self.minHeap[smallest]
            i=smallest
        

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=[[] for _ in range(n+1)]
        for u,v,w in times:
            graph[u].append((v,w))
        heap=MinHeap()
        heap.push((0,k))
        dist=[float("inf")]*(n+1)
        dist[k]=0
        while heap.minHeap:
            d,u=heap.pop()
            if d>dist[u]:
                continue
            for node,wt in graph[u]:
                
                if d+wt<dist[node]:
                    dist[node]=d+wt
                    heap.push((dist[node],node))
        answer=max(dist[1:])
        return answer if answer != float("inf") else -1

        