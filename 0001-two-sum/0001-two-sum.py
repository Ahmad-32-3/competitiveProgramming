class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}

        for i, e in enumerate(nums):
            if (target - e) in map:
                return [i, map[target - e]]
            map[e] = i
            
            