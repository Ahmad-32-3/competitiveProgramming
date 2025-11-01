class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        oak = 0

        l, r = 0, len(nums) - 1
        nums.sort()

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                oak += (2 ** (r-l)) 
                oak = oak % (10**9 + 7)
                l += 1
        
        return oak 