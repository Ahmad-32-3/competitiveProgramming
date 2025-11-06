class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, res = 0, [-1, -1]
        resLen = float("inf")

        need = collections.defaultdict(int)
        window = collections.defaultdict(int)

        have = 0
        need_count = 0

        for r in t:
            need[r] += 1
        
        need_count = len(need)
        
        for r in range(len(s)):
            window[s[r]] += 1

            if window[s[r]] == need[s[r]]:
                have += 1
            
            while have == need_count:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1

                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
            
        l,r = res

        return s[l:r+1] if resLen != float("inf") else ""
                

            
            
