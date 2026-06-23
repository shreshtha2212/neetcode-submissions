class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_left=height[left]
        max_right=height[right]
        summ=0
        while left<right:
            if height[left]<height[right]:
                if max_left-height[left]>=0:
                    summ+=max_left-height[left]
                else:
                    max_left=height[left]
                left+=1
            else:
                if max_right-height[right]>=0:
                    summ+=max_right-height[right]
                else:
                    max_right=height[right]
                right-=1
                
        return summ




        