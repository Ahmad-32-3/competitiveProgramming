class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        leastDiff = float('inf')

        res = 0

        for i in range(len(nums) - 2):
            currNum = nums[i]

            l, r = i + 1, len(nums) - 1

            while l < r:
                left, right = nums[l], nums[r]

                currSum = currNum + left + right

                currDiff = abs(currSum - target)

                if currDiff < leastDiff:
                    leastDiff = currDiff
                    res = currSum
                
                if currSum > target:
                    r -= 1
                elif currSum < target:
                    l += 1
                else:
                    return res
        return res
