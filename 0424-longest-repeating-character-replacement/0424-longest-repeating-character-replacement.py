class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] += 1

            while sum(count.values()) - max(count.values()) > k:
                count[s[l]] -= 1

                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            
            res = max (r - l + 1, res)
        return res