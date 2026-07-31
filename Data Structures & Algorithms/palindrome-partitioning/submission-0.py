class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(s):
            if s==s[::-1]:
                return True
            return False
        ans=[]
        def rec(i,t):
            if  i==len(s):
                ans.append(t.copy())
                return
            for j in range(i,len(s)):
                p=s[i:j+1]

                if isPal(p):
                    t.append(p)
                    rec(j+1,t)
                    t.pop()
        
        rec(0,[])
        return ans

        