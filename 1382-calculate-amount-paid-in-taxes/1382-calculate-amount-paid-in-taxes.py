class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = 0
        left = income
        pv = 0
        for bracket in brackets:
            print(bracket)
            mx = min(bracket[0], left)
            res += (mx - pv)*bracket[1]/100
            pv = mx
            print(mx)
            print(left)
        return res
        