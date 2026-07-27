class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def dfs(t,j,i):
            if t==0:
                ans.append(j.copy())
                return
            if i==len(candidates) or t<0:
                return
            j.append(candidates[i])
            dfs(t-candidates[i], j, i+1)
            j.pop()
            val=candidates[i]
            while i<len(candidates) and candidates[i]==val:
                i+=1
            dfs(t,j,i)
        dfs(target, [],0)
        return ans
        