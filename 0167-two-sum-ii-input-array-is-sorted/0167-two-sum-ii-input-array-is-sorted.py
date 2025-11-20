class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        # [1,2,3,4,5]
        #  0,1,2,3,4
        #numbers[234324] -> parking lot value at lot number left
        while (left < right):
            compare = numbers[left] + numbers[right]
            if compare > target:
                right = right - 1
            if compare < target:
                left = left + 1
            if compare == target:
                return [left + 1, right + 1]
    



