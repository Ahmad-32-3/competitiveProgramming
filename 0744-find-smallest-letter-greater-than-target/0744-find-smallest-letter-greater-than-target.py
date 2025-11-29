class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        flag = False
        while l <= r:
            m = l + ((r-l) // 2)

            if ord(letters[m]) > ord(target):
                r = m - 1
                flag = True
            else:
                l = m + 1
        if flag:
            return letters[l % len(letters)]
        else:
            return letters[0]