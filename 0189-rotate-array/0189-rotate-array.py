class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        length = len(nums) - 1
        k = k % len(nums)
        for i in range(length - k, (length - k) - length -  1, - 1):
            res.append(nums[i])

        res = res[::-1]
        nums[:] = res
        