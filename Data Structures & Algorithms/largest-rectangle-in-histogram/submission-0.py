class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left=[]
        stack=[]
        right=[]
        for i in range(len(heights)):
            if not stack:
                left.append(0)
                stack.append(i)
            elif heights[i]<=heights[stack[-1]]:
                
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                if stack==[]:
                    left.append(0)
                else:
                    left.append(stack[-1]+1)
                stack.append(i)
            elif heights[i]>heights[stack[-1]]:
                left.append(stack[-1]+1)
                stack.append(i)
                
        while stack: 
            stack.pop()
        for j in range(len(heights)-1,-1,-1):
            if not stack:
                right.append(len(heights)-1)
                stack.append(j)
            elif heights[j]<=heights[stack[-1]]:
                
                while stack and heights[stack[-1]]>=heights[j]:
                    stack.pop()
                if stack==[]:
                    right.append(len(heights)-1)
                else:
                    right.append(stack[-1]-1)
                stack.append(j)
            elif heights[j]>heights[stack[-1]]:
                right.append(stack[-1]-1)
                stack.append(j)
                
        right=right[::-1]
        maxAr=float("-inf")
        for i in range(len(heights)):
            ar=(right[i]-left[i]+1)*heights[i]
            maxAr=max(maxAr,ar)
        return maxAr




        