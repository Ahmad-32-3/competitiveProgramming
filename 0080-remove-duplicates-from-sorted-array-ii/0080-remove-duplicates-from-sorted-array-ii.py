class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        builder = 0

        for num in nums:
            if builder < 2 or num > nums[builder - 2]:
                nums[builder] = num
                builder += 1

        return builder  
        