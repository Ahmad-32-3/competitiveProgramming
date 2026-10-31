class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ans = defaultdict(int)

        for c in ransomNote:
            ans[c] += 1
        
        for c in magazine:
            ork = ans[c] - 1 
            if ork >= 0:
                ans[c] -= 1

        return sum(ans.values()) == 0