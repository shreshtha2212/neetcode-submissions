class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        freq_list=[]
        for num,count in freq.items():
            freq_list.append((count,num))
        freq_list.sort(reverse=True)
        ans=[]
        
        for i in range(k):
            ans.append(freq_list[i][1])
        return ans

        