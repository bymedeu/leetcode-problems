class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 1

        aLen = len(nums1)
        bLen = len(nums2)

        while i < aLen and j < bLen:
            i += nums1[i] > nums2[j]
            j += 1
        
        return j - i - 1
