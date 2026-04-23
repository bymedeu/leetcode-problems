from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dico = defaultdict(list)
        for i, n in enumerate(nums):
            dico[n].append(i)

        arr = [0] * len(nums)
        
        for val in dico.values():
            tot = sum(val)
            ls = 0
            lV = len(val)

            for i in range(lV):
                rs = tot - ls - val[i]

                left = val[i] * i - ls
                right = rs - val[i] * (lV - i - 1)

                arr[val[i]] = left + right

                ls += val[i]

        return arr
        