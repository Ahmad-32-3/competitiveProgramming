class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, oak = 0, 0
        res = 0

        for r in range(len(s)):
            if s[r] != s[l]:
                oak += 1
            
            while oak > k:
                l += 1
                if s[l] == s[r]:
                    oak -= 1
            
            res = max(r - l + 1, res)
        
        return res