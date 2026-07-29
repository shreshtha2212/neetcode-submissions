class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def getPerm(i,arr,ans):
            if i==len(nums):
                ans.append(arr.copy())
                return
            for idx in range(i,len(arr)):
                arr[i],arr[idx]=arr[idx],arr[i]
                getPerm(i+1,arr,ans)
                arr[i],arr[idx]=arr[idx],arr[i]
        ans=[]
        getPerm(0,nums,ans)
        return ans

        