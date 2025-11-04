class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = collections.defaultdict(int)
        s_dict = collections.defaultdict(int)

        l = 0
        res = []

        for r in p:
            p_dict[r] += 1
        
        
        for r in range(len(s)):
            s_dict[s[r]] += 1

            if r - l + 1 > len(p):
                s_dict[s[l]] -= 1
                if s_dict[s[l]] == 0:
                    del s_dict[s[l]]
                l += 1

                
            
            
            if p_dict == s_dict:
                res.append(l)
        
        return res