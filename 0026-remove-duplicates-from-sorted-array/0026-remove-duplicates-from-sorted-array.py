class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        visited = set()
        ork = []
        for r in range(len(nums)):
            if nums[r] not in visited:
                ork.append(nums[r])
                visited.add(nums[r])
                
        nums[:] = ork
        res = len(visited)
        return res
        