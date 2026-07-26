class MedianFinder:

    def __init__(self):
        self.max_heap=[]
        self.min_heap=[]
        

    def addNum(self, num: int) -> None:
        
        self.build_max_heap(self.max_heap,num)
        if self.min_heap and self.max_heap[0]>self.min_heap[0]:
            value=self.pop_max(self.max_heap)
            self.build_min_heap(self.min_heap, value)
        if len(self.max_heap)>len(self.min_heap)+1:
            value=self.pop_max(self.max_heap)
            self.build_min_heap(self.min_heap,value)
        if len(self.min_heap)>len(self.max_heap)+1:
            value=self.pop_min(self.min_heap)
            self.build_max_heap(self.max_heap,value)
        

    def findMedian(self) -> float:
        if len(self.min_heap)>len(self.max_heap):
            return float(self.min_heap[0])
        if len(self.max_heap)>len(self.min_heap):
            return float(self.max_heap[0])
        return (self.max_heap[0]+self.min_heap[0])/2

    def build_max_heap(self, max_heap:List[int],num: int)->None:
        self.max_heap.append(num)
        i=len(max_heap)-1
        while i>0:
            p=(i-1)//2
            if max_heap[p]<max_heap[i]:
                max_heap[p],max_heap[i]=max_heap[i],max_heap[p]
            i=p
    def build_min_heap(self, min_heap:List[int], num: int)->None:
        self.min_heap.append(num)
        i=len(min_heap)-1
        while i>0:
            p=(i-1)//2
            if min_heap[i]<min_heap[p]:
                min_heap[p],min_heap[i]=min_heap[i],min_heap[p]
            i=p
    def heapify_down_max(self,max_heap:List[int])->None:
        i=0
        largest=i
        while True:
            left=2*i+1
            right=2*i+2
            if left<len(self.max_heap) and max_heap[left]>max_heap[largest]:
                largest=left
            if right<len(self.max_heap) and max_heap[right]>max_heap[largest]:
                largest=right
            if largest==i:
                break
            max_heap[largest],max_heap[i]=max_heap[i],max_heap[largest]
            i=largest
    def heapify_down_min(self,min_heap:List[int])->None:
        i=0
        smallest=i
        while True:
            left=2*i+1
            right=2*i+2
            if left<len(self.min_heap) and min_heap[left]<min_heap[smallest]:
                smallest=left
            if right<len(self.min_heap) and min_heap[right]<min_heap[smallest]:
                smallest=right
            if smallest==i:
                break
            min_heap[smallest],min_heap[i]=min_heap[i],min_heap[smallest]
            i=smallest
    def pop_max(self,max_heap:List[int])->int:
        j=max_heap[0]
        max_heap[0]=max_heap[-1]
        max_heap.pop()
        self.heapify_down_max(self.max_heap)
        return j
    def pop_min(self,min_heap:List[int])->int:
        j=min_heap[0]
        min_heap[0]=min_heap[-1]
        min_heap.pop()
        self.heapify_down_min(self.min_heap)
        return j
        
            
            
    



        
        