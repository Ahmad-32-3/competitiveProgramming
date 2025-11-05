class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # if frequency[r] == 0
        # then: 
        # - while frequency[l] == 0 and l <= r"
        # if l == r
        # append
        # naturally break and continue adding to r if it doesnt fulfill the while conditions
        frequency = collections.defaultdict(int)
        l, res = 0, []
        oak = 0
        for i in s:
            frequency[i] += 1

        print(frequency)

        for r in range(len(s)):
            frequency[s[r]] -= 1
            print("right: ", r, "left", l)
            print("frequency[r]: ", frequency[s[r]])
            print("oak: ", oak)
            if frequency[s[r]] == 0:
                while frequency[s[l]] == 0 and l <= r:
                    if l == r:
                        res.append(r - oak + 1)
                        oak = l + 1
                        break
                    l += 1
    
        if len(res) == 0:
            return [len(s)]
        else:
            return res