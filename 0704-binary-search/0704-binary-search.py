class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nlen = len(nums)
        l, r = 0, len(nums) - 1

        while (l <= r):
            M = (r + l) // 2

            if nums[M] > target:
                r = M - 1
            elif nums[M] < target:
                l = M + 1
            else:
                return M
            nlen = nlen // 2
        return -1