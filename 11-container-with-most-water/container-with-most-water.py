class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            distance = r - l

            currArea = distance * min(height[l], height[r])

            if currArea > area:
                area = currArea

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return area
            