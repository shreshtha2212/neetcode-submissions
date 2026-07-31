class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsToChar={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        ans=[]
        def bT(i,c):
            if i==len(digits):
                ans.append(c)
                return
            for t in digitsToChar[digits[i]]:
                c+=t
                bT(i+1,c)
                c = c[:-1]
        if digits:
            bT(0,"")
            return ans
        else:
            return []
        
        