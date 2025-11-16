class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        average = float('-inf')
        l = 0
        runSum = float(0)
        for r in range(len(nums)):
            runSum += nums[r]
            print(runSum)
            if r - l + 1 == k:
                average = max(average, runSum / k)
                runSum -= nums[l]
                l += 1
        return average