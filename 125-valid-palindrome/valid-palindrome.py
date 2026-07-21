class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for c in s:
            if c.isalnum():
                word += c.lower()
        
        if word == word[::-1]:
            return True
        return False
        