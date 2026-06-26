class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q=deque([])
        ans=[]
        for i in range(k):
            while q and q[-1]<nums[i]:
                q.pop()
            q.append(nums[i])
        ans.append(q[0])
        for i in range(k,len(nums)):
            if q[0]==nums[i-k]:
                q.popleft()
            while q and q[-1]<nums[i]:
                q.pop()
            q.append(nums[i])
            ans.append(q[0])
        return ans
            
