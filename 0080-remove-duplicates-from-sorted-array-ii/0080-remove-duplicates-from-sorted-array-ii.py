class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        counter = 0
        l = 0
        currElement = nums[l]
        for r in range(len(nums)):
            if nums[r] == currElement:
                counter += 1
            else:
                if counter >= 2:
                    nums[l] = nums[r-1]
                    nums[l+1] = nums[r-1]
                    l += 2
                    counter = 1
                    currElement = nums[r]
                else:
                    nums[l] = nums[r-1]
                    l += 1
                    counter = 1
                    currElement = nums[r]

        if counter >= 2:
            nums[l] = currElement
            nums[l+1] = currElement
        elif counter == 1:
            nums[l] = currElement

        if counter >= 2:
            return l + 2
        else:
            return l + 1

        