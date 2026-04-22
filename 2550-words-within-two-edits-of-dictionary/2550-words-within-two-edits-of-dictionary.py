class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        def dist(s1 : str, s2 :str):
            cpt = 0
            for a, b in zip(s1, s2):
                cpt += a != b
                if cpt > 2:
                    return False
            return True

        res = []

        for q in queries:
            for d in dictionary:
                if len(q) == len(d) and dist(q, d):
                    #print(f"{q} approved by {d}")
                    res.append(q)
                    break

        
        return res

        