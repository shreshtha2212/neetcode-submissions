class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=[0]*26
        count=0
        
        for i in range(len(tasks)):
            index = ord(tasks[i]) - ord('A')
            freq[index] += 1
            count=max(count,freq[index])
        ans=(count-1)*(n+1)
        for i in range(len(freq)):
            if freq[i]==count:
                ans+=1
        return max(ans,len(tasks))
        