class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        lS = len(source)
        parent = [i for i in range(lS)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def unite(a, b):
            parent[find(a)] = find(b)

        for a, b in allowedSwaps:
            unite(a, b)

        freq = defaultdict(Counter)
        for i in range(lS):
            freq[find(i)][source[i]] += 1
        
        hd = 0

        for i in range(lS):
            root = find(i)
            if freq[root][target[i]] > 0:
                freq[root][target[i]] -= 1
            else:
                hd += 1
        
        return hd