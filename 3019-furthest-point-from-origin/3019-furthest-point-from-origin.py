class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = 0
        r = 0
        a = 0
        for c in moves:
            if c == '_':
                a += 1
            elif c == 'L':
                l += 1
            else:
                r += 1

        return max(abs(r - l - a), abs(r - l + a)) 