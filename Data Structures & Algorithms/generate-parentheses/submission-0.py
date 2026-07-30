class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(o,c,ans,cur):
            if o==c==n:
                j="".join(cur)
                ans.append(j)
                return
            if o<n:
                cur.append("(")
                
                gen(o+1,c,ans,cur)
                
                cur.pop()
            
                
            if c<o:
                cur.append(")")
                
                gen(o,c+1,ans,cur)
                
                cur.pop()
        ans=[]
        gen(0,0,ans,[])
        return ans
            
            
        