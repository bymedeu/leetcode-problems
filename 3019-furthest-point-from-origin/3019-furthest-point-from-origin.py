class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        d = 0
        a = 0
        for c in moves:
            if c == '_':
                a += 1
            elif c == 'L':
                d -= 1
            else:
                d += 1
        return abs(d) + a

