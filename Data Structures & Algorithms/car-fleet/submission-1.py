class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans=slow_car=0
        for i,j in sorted(zip(position,speed), reverse=True):
            eta=(target-i)/j
            if eta>slow_car:
                slow_car=eta
                ans+=1
        return ans

        