class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        orig = 0
        while x > 0:
            orig = orig * 10 + x % 10
            x = x // 10
        res = orig * sign
        if res > 2**31-1:
            return 0 
        if res < -2**31:
            return 0
        return res


        