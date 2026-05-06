class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n = len(boxGrid)
        m = len(boxGrid[0])
        box = [['.' for _ in range(n)] for _ in range(m)]

        for r in range(n):
            p = m - 1
            for c in range(m - 1, -1, -1):
                if boxGrid[r][c] == '*':
                    box[c][n - 1 - r] = '*'
                    p = c - 1
                elif boxGrid[r][c] == '#':
                    box[p][n- 1 - r] = '#'
                    p -= 1
        
        return box
