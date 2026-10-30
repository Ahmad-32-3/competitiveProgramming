class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        ans = set()

        for e in nums:
            if e in ans:
                return True
            ans.add(e)

        return False