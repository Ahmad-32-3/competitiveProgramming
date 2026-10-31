class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ork = defaultdict(int)
        currTotal = 0
        res = 0
        ork[0] = 1
        for r in range(len(nums)):
            currTotal += nums[r]
            if currTotal - k in ork:
                res += (ork[currTotal-k])
            ork[currTotal] += 1

        return res


            
