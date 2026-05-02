class Solution:
    def rotatedDigits(self, n: int) -> int:
        dp = [0 for i in range(1 + n)]
        for i in range(0, min(10, n + 1)):
            if i in (0, 1 , 8):
                dp[i] = 1
            if i in (2, 5, 6, 9):
                dp[i] = 2
        for i in range(10, n + 1):
            a = dp[i % 10]
            b = dp[i // 10]
            if a == 1 and b == 1:
                dp[i] = 1
            elif a >= 1 and b >= 1:
                dp[i] = 2
        #print(dp) 
        return dp.count(2)
                

