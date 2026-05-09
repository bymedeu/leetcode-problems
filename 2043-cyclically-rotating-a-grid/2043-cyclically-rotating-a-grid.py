class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        m = len(grid)
        n = len(grid[0])
        arrs = [[] for _ in range(m // 2)]
        for i in range(m // 2):
            #print(f"cycle {i + 1}")
            #print("top line")
            for j in range(i, n - i):
                #print(i, j)
                arrs[i].append(grid[i][j])
            #print("right row")
            for j in range(i + 1, m - i - 1):
                arrs[i].append(grid[j][n - 1 - i])
                #print(j, n - 1)
            #print("bot line")
            for j in range(i, n - i):
                arrs[i].append(grid[m - i - 1][n - 1 - j])
                #print(m - i - 1, n - 1 - j)
            print("left row")
            for j in range(m - i - 2, i, -1):
                arrs[i].append(grid[j][i])
                print(j, 0)

        #print(arrs)

        for i in range(m // 2):
            tmp = arrs[i][k:] + arrs[i][:k]
            arrs[i] = tmp

        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m // 2):
            print(arrs[i])
            k = 0
            for j in range(i, n - i):
                #print(i, j)#
                res[i][j] = arrs[i][k]
                k += 1
            #print("right row")
            for j in range(i + 1, m - i - 1):
                res[j][n - 1 - i] = arrs[i][k]
                k += 1
                #print(j, n - 1)
            #print("bot line")
            for j in range(i, n - i):
                res[m - i - 1][n - 1 - j] = arrs[i][k]
                k += 1
                #print(m - i - 1, n - 1 - j)
            #print("le^t row")
            for j in range(m - i - 2, i, -1):
                res[j][i] = arrs[i][k]
                print(arrs[i][k])
                k += 1
                #print(i, n - 1)


        return res
        """
        top = 0
        left = 0
        bottom = len(grid) - 1
        right = len(grid[0]) - 1

        while top < bottom and left < right:
            length = bottom - top
            width = right - left
            p = 2 * length + 2 * width
            r = k % p

            while r:
                tmp = grid[top][left]

                for i in range(left, right):
                    grid[top][i] = grid[top][i + 1]
                for i in range(top, bottom):
                    grid[i][right] = grid[i + 1][right]
                for i in range(right, left, -1):
                    grid[bottom][i] = grid[bottom][i - 1]
                for i in range(bottom, top, -1):
                    grid[i][left] = grid[i - 1][left]
                
                grid[top + 1][left] = tmp
                r -= 1
            
            top += 1
            left += 1
            bottom -= 1
            right -= 1
        return grid