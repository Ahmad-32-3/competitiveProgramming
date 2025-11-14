class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        if not nums:
            return 0

        for i, e in enumerate(nums):
            visited.add(e)
        res = 0
        while nums:
            target = nums.pop()
            ork = 0
            if target - 1 not in visited:
                while target + 1 in visited:
                    ork += 1
                    res = max(res, ork)
                    target = target + 1
                    visited.remove(target)

        return res + 1

        
        