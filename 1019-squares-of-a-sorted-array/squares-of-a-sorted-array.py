class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = []

        while l <= r:
            if l != r:
                left_square = nums[l] * nums[l]
                right_square = nums[r] * nums[r]

                if left_square > right_square:
                    res.append(left_square)
                    l += 1
                else:
                    res.append(right_square)
                    r -= 1
            else:
                res.append(nums[l] * nums[r])
                l += 1
        
        return res[::-1]

