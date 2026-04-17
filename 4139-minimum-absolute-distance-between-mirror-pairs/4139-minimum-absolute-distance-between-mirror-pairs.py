class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        hm = {}
        ans = 100000

        numLen = len(nums)
        for i in range(numLen):
            rvsd = [int(str(nums[i])[::-1])][0]
            if nums[i] in hm:
                ans = min(ans, i - hm[nums[i]])
            hm[rvsd] = i
        
        

        if ans == 100000:
            return -1
        return ans
        