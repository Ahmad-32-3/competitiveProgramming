class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        previousElement = {}
        # iterate through list
        # check if target - element exists in the hashmap
        # if yes, then return the indices of the hashmap
        # if not, then append the element to key and append the index of the element to value

        for i, e in enumerate(nums):
            diff = target - e
            if diff in previousElement:
                return [previousElement[diff], i]
            previousElement[e] = i
        return 
            