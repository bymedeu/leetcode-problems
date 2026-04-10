class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        max = 1
        s_len = len(s)
        for i in range(s_len):
            hash = []
            cpt = 0
            for j in range(i, s_len):
                if (s[j] not in hash):
                    cpt += 1
                    hash.append(s[j])
                else:
                    break
            if (cpt > max):
                max = cpt
        return max

            
        
        