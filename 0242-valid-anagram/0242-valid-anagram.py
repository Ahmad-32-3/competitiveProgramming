class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = defaultdict(int)
        for c in s:
            map[c] += 1
        
        map2 = defaultdict(int)
        for c in t:
            map2[c] += 1

        
        return map == map2