class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        l = 0
        res = 0
        oak = 0

        for r in range(len(s)):
            count[s[r]] += 1
            oak = max(oak, count[s[r]])

            while (r - l + 1) - oak > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)
        return res