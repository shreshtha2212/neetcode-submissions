class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.p=[]
        for i in stones:
            self.push(i)
        while len(self.p)>1:
            first=self.pop()
            second=self.pop()
            if first!=second:
                self.push(first-second)
        return self.p[0] if self.p else 0
            
    def push(self, val)->None:
        self.p.append(val)
        i=len(self.p)-1
        while i>0:
            pa=(i-1)//2
            if self.p[pa]>=self.p[i]:
                break
            self.p[pa],self.p[i]=self.p[i],self.p[pa]
            i=pa
    def pop(self)->int:
        largest=self.p[0]
        last=self.p.pop()
        if self.p:
            self.p[0]=last
            self.heapify_down(0)
        return largest
    def heapify_down(self,i)->None:
        while True:
            largest=i
            left=2*i+1
            right=2*i+2
            if left<len(self.p) and self.p[left]>self.p[largest]:
                largest=left
            if right<len(self.p) and self.p[right]>self.p[largest]:
                largest=right
            if largest==i:
                break
            self.p[i],self.p[largest]=self.p[largest],self.p[i]
            i=largest
        
            




            


        

        