class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequency = collections.defaultdict(int)
        s2_dict = collections.defaultdict(int)

        l = 0
        count = 0

        for r in s1:
            frequency[r] += 1
        
        for r in range(len(s2)):
            s2_dict[s2[r]] += 1

            if r - l + 1 > len(s1):
                s2_dict[s2[l]] -= 1
                if s2_dict[s2[l]] == 0:
                    del s2_dict[s2[l]]
                l += 1

            if frequency == s2_dict:
                    return True

        return False
            
        
        
        