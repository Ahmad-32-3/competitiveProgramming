class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        #[-4,-1,1,2]
        for i in range(len(nums)):
            ork = nums[i]
            l = i + 1
            r = len(nums) - 1  

            while l < r:
                runSum = ork + nums[l] + nums[r]

                if abs(runSum - target) < abs(res - target):
                    res = runSum
                if runSum > target:
                    r -= 1
                elif runSum < target:
                    l += 1
                else:
                    return runSum
        return res
