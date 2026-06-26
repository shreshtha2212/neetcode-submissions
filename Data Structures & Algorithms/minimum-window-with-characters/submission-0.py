class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        have={}
        l=0
        required=len(need)
        formed=0
        res=[-1,-1]
        minLen=float("inf")
        for r in range(len(s)):
            have[s[r]] = have.get(s[r], 0) + 1
            if s[r] in need and have[s[r]]==need[s[r]]:
                formed+=1
            while formed==required:
                if (r-l+1)<minLen:
                    minLen=r-l+1
                    res=[l,r]
                have[s[l]]-=1
                if s[l] in need and have[s[l]]<need[s[l]]:
                    formed-=1
                l+=1
            
        return "" if minLen==float("inf") else s[res[0]:res[1]+1]
            
       
            
