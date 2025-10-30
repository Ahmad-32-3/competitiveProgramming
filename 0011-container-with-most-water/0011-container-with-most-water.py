class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        
        l, r = 0, len(height) - 1

        
        for i, e in enumerate(height):
            currArea = min(height[l],height[r]) * (r-l)
            maxArea = max(currArea,maxArea)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxArea
        
        


