class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(m, piles):
            s=0
            for i in range(len(piles)):
                s+=(piles[i]+m-1)//m
            return s
        l=1
        r=max(piles)
        ans=0
        while l<=r:
            mid=(l+r)//2
            if check(mid, piles)<=h:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans

        