class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        # [3,3,4,5]
        ork = 0
        l, r = 0, len(people) - 1

        while l <= r:
            currTot = people[r] + people[l]

            if currTot > limit:
                ork += 1
                r -= 1
            else:
                ork += 1
                r -= 1
                l += 1
        return ork
