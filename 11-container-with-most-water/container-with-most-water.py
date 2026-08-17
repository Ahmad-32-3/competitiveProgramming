class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            currArea = min(height[l], height[r]) * (r - l)

            area = max(area, currArea)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area