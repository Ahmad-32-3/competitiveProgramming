class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # a + b > c : triangle
        # a <= b <= c
        # compare a and b with c and then make a conclusion

        nums.sort()
        res = 0
        # [1,2,3,4,4,5,6,8,9]

        for i in range(len(nums) - 1, -1, -1):
            c = nums[i]

            l, r = 0, i - 1

            while l < r:
                a, b = nums[l], nums[r]
                if a + b > c:
                    # all values of a such that a <= b are valid, meaning window from a to b is valid
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res