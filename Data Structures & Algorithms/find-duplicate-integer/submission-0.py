class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0
        while True:
            slow=nums[slow] #move slow one step
            fast=nums[nums[fast]] #move fast 2 steps
            if slow==fast:
                break
            
        slow=0
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow
        