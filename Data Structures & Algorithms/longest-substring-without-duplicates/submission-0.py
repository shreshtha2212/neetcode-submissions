class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        ans=0
        k=[]
        for r in range(len(s)):
            while s[r] in k:
                k.remove(s[l])
                l+=1
            k.append(s[r])
            ans = max(ans, len(k))
        return ans