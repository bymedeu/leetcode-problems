class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        lC = len(colors)

        for i in range(lC):
            if colors[i] != colors[-1] or colors[-1 - i] != colors[0]:
                return lC - 1 - i
        
        return 0
        