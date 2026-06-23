class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h=defaultdict(int)
        for i in range(len(numbers)):
            if target-numbers[i] in h:
                return [h[target-numbers[i]],i+1]
            h[numbers[i]]=i+1

        