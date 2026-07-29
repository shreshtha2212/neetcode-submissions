class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def sub(ans, i,s):
            if i==len(nums):
                ans.append(s.copy())
                return
            s.append(nums[i])
            sub(ans,i+1,s)
            s.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            sub(ans,i+1,s)
        ans=[]
        sub(ans,0,[])
        return ans
        