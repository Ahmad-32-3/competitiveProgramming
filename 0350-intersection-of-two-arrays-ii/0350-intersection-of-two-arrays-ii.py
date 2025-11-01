class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary = {}
        list = []


        for i, e in enumerate(nums1):
            if e not in dictionary:
                dictionary[e] = 1
            else:
                dictionary[e] += 1

        for i, e in enumerate(nums2):
            if e in dictionary:
                if dictionary[e] == 0:
                    pass
                else:
                    list.append(e)
                    dictionary[e] -= 1

        return list