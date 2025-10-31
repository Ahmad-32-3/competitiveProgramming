class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        array = []
        while l <= r:
            if nums[r]*nums[r] > nums[l]*nums[l]:
                array.append(nums[r]*nums[r])
                r -= 1
            else:
                array.append(nums[l]*nums[l])
                l += 1
        return array[::-1]

