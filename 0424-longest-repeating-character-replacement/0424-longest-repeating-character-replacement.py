class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0

        oak = collections.defaultdict(int)

        count = 0

        for r in range(len(s)):
            oak[s[r]] += 1

            count = max(count, oak[s[r]])

            while (r - l + 1) - count > k:
                oak[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res