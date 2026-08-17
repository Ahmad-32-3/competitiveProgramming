class Solution:
    def reverseVowels(self, s: str) -> str:
        sD = list(s)
        l, r = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        while l < r:
            if sD[r].lower() not in vowels:
                r -= 1
                continue
            if sD[l].lower() not in vowels:
                l += 1
                continue
            if sD[l].lower() and sD[r].lower() in vowels:
                sD[l], sD[r] = sD[r], sD[l]
                l += 1
                r -= 1
            
        return "".join(sD)