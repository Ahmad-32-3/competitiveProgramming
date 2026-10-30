class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ork = set()
        res = 0
        counter = 0
        for n in nums:
            ork.add(n)

        for key in ork:
            if key - 1 not in ork:
                while key + counter in ork:
                    counter += 1
                res = max(res, counter)
                counter = 0

        return res