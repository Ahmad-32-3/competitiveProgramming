class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        ans = collections.defaultdict(int)

        for num in nums:
            ans[num] += 1
        
        for key in ans:
            if ans[key] > 1:
                return True
        
        return False