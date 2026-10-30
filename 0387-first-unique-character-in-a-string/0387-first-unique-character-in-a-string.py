class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = defaultdict(int)
        for c in s:
            ans[c] += 1

        for i in range(len(s)):
            if ans[s[i]] < 2:
                return i
        return -1 