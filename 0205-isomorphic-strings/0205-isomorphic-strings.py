class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ans = defaultdict(list)
        ork = defaultdict(list)
        for c in range(len(s)):
            ans[s[c]].append(c)
        for c in range(len(t)):
            ork[t[c]].append(c)
        
        return list(ans.values()) == list(ork.values())