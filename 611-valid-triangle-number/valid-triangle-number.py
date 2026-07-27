class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # a + b > c
        # a + c > b
        # b + c > a

        nums.sort()
        res = 0

        for i in range(len(nums) - 1, -1, -1):
            l, r = 0, i - 1
            
            c = nums[i]
            while l < r:
                a, b = nums[l], nums[r]

                if a + b <= c:
                    l += 1
                else:
                    res += r - l 
                    r -= 1
        return res  
            