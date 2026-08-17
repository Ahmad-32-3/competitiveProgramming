class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        s = s.lower()
        for e in s:
            if e.isalnum():
                word += e
        return word == word[::-1]