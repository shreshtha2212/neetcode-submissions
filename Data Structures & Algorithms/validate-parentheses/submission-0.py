class Solution:
    def isValid(self, s: str) -> bool:
        h={"{":"}","[":"]","(":")"}
        stack=[]
        for i in s:
            if i in h:
                stack.append(i)
            else:
                if not stack:
                    return False
                
                if h[stack[-1]]!=i:
                    return False
                stack.pop()
        return stack==[]
        