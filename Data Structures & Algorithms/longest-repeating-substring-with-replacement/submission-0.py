class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap={}
        res=0
        maxF=0
        l=0
        for r in range(len(s)):
            hashMap[s[r]]=hashMap.get(s[r],0)+1
            maxF=max(maxF,hashMap[s[r]])
            while (r-l+1)-maxF>k:
                hashMap[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
        