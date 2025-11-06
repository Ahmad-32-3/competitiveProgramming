class Solution:
    def atMost(self, nums, k):
        l, res = 0, 0

        count = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                count += 1
            
            while count > k:
                if nums[l] % 2 == 1:
                    count -= 1
                l += 1
                
            
            res += r - l + 1
        
        return res

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums,k) - self.atMost(nums,k-1)
        