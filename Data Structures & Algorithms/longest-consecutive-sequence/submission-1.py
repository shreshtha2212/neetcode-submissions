class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ans=1
        for i in nums:
            cnt=1
            if i-1 in nums:
                continue
            elif i+1 in nums:
                j=i+1
                
                while j in nums:
                    cnt+=1
                    j=j+1
            ans=max(ans,cnt)
            
        return ans

        