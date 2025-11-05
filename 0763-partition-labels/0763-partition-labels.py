class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        frequency = collections.defaultdict(int)
        l, res = 0, []
        oak = 0
        for i in s:
            frequency[i] += 1

        for r in range(len(s)):
            frequency[s[r]] -= 1

            if frequency[s[r]] == 0:
                while frequency[s[l]] == 0 and l <= r:
                    if l == r:
                        res.append(r - oak + 1)
                        oak = l + 1
                        break
                    l += 1
    
        return res