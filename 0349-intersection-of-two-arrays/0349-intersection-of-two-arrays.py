class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        visited = set()
        res = []
        for e in nums1:
            visited.add(e)
        
        for i in range(len(nums2)):
            if nums2[i] in visited:
                res.append(nums2[i])
                visited.remove(nums2[i])
        return res