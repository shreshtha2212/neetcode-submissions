class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def dfs(t,l,i):
            
            if i==len(nums) or t<0:
                return
            if t==0:
                ans.append(l.copy())
                return
            l.append(nums[i])
            dfs(t-nums[i],l,i)
            l.pop()
            dfs(t,l,i+1)
        dfs(target,[],0)
        return ans

