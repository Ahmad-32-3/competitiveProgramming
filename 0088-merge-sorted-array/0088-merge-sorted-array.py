class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
       
        one = m - 1 
        two = n - 1

        for i in range(m+n-1, -1, -1):
            if two == -1:
                break
            
            if one == -1:
                nums1[i] = nums2[two]
                two -= 1
            elif nums2[two] > nums1[one]:
                nums1[i] = nums2[two]
                two -= 1
            else:
                nums1[i] = nums1[one]
                one -= 1
        
        