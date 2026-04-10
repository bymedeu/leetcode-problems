class Solution:
    def median_of_list(self, l: List[int], ll: int) -> float:
        if ll % 2:
            return l[ll // 2]
        return (l[ll // 2 - 1] + l[ll // 2]) / 2

        
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
 
        len1 = len(nums1)
        len2 = len(nums2)
        
        if len1 == 0:
            return self.median_of_list(nums2, len2)
        if len2 == 0:
            return self.median_of_list(nums1, len1)
            
        imin = nums1[0]
        jmin = nums2[0]
        l = []
        i = 0
        j = 0
        
        while i < len1 or j < len2:
            if imin < jmin:
                l.append(imin)
                i += 1
                if i >= len1:
                    imin = math.inf
                else:
                    imin = nums1[i]
            else:
                l.append(jmin)
                j += 1
                if j >= len2:
                    jmin = math.inf
                else:
                    jmin = nums2[j]
        
        ll = len1 + len2
        return self.median_of_list(l, ll)