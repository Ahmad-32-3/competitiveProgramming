class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        visited = set()
        runSum = 0

        for i in range(n):
            visited.add(nums[i])
        
        # [3,0,1]
        # = 3
        # while runSum != n:
        # if runSum + 1 in visited
        #     runSum += 1
        # else: 
        #      return runSum + 1
        for i in range(n):
            if nums[i] == 0:
                while runSum != n:
                    if runSum + 1 in visited:
                        runSum += 1
                    else:
                        return runSum + 1
        return 0