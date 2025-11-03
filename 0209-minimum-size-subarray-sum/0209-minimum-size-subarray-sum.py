class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, tot = 0, 0

        sol = float("inf")

        for r in range(len(nums)):
            tot += nums[r]

            while tot >= target:
                sol = min(r-l+1,sol)
                tot -= nums[l]
                l += 1

        return 0 if sol == float("inf") else sol
                