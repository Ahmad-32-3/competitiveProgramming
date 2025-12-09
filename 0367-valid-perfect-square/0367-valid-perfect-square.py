class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ork = int(sqrt(num))

        return ork * ork == num