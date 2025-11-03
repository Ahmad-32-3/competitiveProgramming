class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        frequency = collections.defaultdict(int)
        l, res = 0, 0

        for r in range(len(s)):
            frequency[s[r]] += 1
            print(s[r])

            while frequency[s[r]] > 1:
                frequency[s[l]] -= 1
                l += 1
            
            print(l)
            res = max(r - l + 1, res)
        
        return res
            
