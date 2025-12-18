class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        
        while l < r:

            m = l + ((r - l) // 2) 

            if nums[m] < nums[m+1]:
                l = m + 1
            else:
                r = m - 1
        
        return r