class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ork = float('inf')
        res = 0
        nums.sort()
        for i in range(len(nums) - 2):
            e = nums[i]

            l, r = i + 1, len(nums) - 1

            while l < r:
                left = nums[l]
                right = nums[r]
                currSum = e + left + right
                currOrk = abs(currSum - target)
                if currOrk <= ork:
                    ork = currOrk
                    res = currSum

                if currSum > target:
                    r -= 1
                elif currSum < target:
                    l += 1
                else:
                    return res
        return res