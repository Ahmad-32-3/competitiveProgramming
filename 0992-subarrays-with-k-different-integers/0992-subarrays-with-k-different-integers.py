class Solution:
    def atMost(self, nums, k):
        frequency = collections.defaultdict(int)
        oak = collections.defaultdict(int)
        countOne = 0
        l = 0

        for r in range(len(nums)):
            
            frequency[nums[r]] += 1

            while len(frequency) > k and l <= r:
                frequency[nums[l]] -= 1
                if frequency[nums[l]] == 0:
                    del frequency[nums[l]]
                l += 1
            

            countOne += r - l + 1
        return countOne
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
 
        return self.atMost(nums, k) - self.atMost(nums, k - 1)
        