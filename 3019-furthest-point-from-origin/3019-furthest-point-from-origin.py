class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
       l = moves.count("L")
       r = moves.count("R")
       a = len(moves) - l - r
       return max(abs(r - l - a), abs(r - l + a)) 