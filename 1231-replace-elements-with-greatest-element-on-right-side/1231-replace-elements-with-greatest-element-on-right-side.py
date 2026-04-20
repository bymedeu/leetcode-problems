class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = -1
        lA = len(arr)
        for i in range(lA - 1,  -1, -1):
            arr[i], maxx = maxx, max(maxx, arr[i])
        return arr

        