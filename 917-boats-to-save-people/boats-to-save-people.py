class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l, r = 0, len(people) - 1
        while l <= r:
            currSum = people[l] +people[r]
            if currSum > limit:
                res += 1
                r -= 1
            else:
                res += 1
                r -= 1
                l += 1
        return res
