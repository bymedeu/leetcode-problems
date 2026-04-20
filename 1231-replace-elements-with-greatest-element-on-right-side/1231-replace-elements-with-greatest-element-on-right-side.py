class Solution:
    def getMaxIndex(self, start: int, arr: List[int]):
        lenA = len(arr)
        maxx = start + 1
        for i in range(start + 1, lenA):
            if arr[i] > arr[maxx]:
                maxx = i
        return maxx

    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        lenA = len(arr)
        res = []
        while i < lenA - 1:
            maxId = self.getMaxIndex(i, arr)
            while i < maxId:
                res.append(arr[maxId])
                i += 1
                print("appended at ", i)
            print(i, maxId)
        res.append(-1)
        return res

        