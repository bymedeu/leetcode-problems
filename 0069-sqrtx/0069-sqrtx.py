class Solution:
    def mySqrt(self, x: int) -> int:
        curr = 1
        while curr * curr <= x:
            curr += 1
        return curr - 1