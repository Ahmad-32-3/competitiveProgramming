class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for r, e in enumerate(nums):
            if e != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1                
            