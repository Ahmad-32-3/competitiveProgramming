class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        oak = 0
        while l <= r:
            if people[l] + people[r] > limit:
                oak += 1
                r -= 1
            else:
                oak += 1
                l += 1
                r -= 1
        
        return oak

    # [1,2,2,3]