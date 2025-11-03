class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        frequency = collections.defaultdict(int)
        l, res = 0,0

        for r in range(len(nums)):
            frequency[nums[r]] += 1

            while frequency[0] > k:
                frequency[nums[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        
        return res
        