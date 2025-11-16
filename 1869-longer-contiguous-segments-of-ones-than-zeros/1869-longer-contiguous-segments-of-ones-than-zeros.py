class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zlen = 0
        ork = 0
        olen = 0
        oak = 0
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] != s[l]:
                if s[l] == '0':
                    zlen -= 1
                else:
                    olen -= 1
                l += 1

            if s[r] == '0':
                zlen += 1
            else:
                olen += 1

            ork = max(ork, zlen)
            oak = max(oak, olen)

        if oak > ork:
            return True
        else:
            return False

        

            
            
            