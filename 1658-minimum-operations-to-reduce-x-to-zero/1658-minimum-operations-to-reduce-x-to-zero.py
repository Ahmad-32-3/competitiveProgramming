class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # total = target + count
        # count = total - x
        l = 0
        count = 0
        maxLen = -1
        total = sum(nums)
        target = total - x
        for r in range(len(nums)):
            count += nums[r]

            while l <= r and count > target:
                count -= nums[l]
                l += 1
            
            if count == target:
                maxLen = max((r - l + 1), maxLen)

        return maxLen if maxLen == -1 else len(nums) - maxLen
