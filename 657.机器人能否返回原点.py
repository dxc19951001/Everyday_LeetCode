from collections import Counter

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ans = Counter(moves)
        return ans['L'] == ans['R'] and ans['U'] == ans['D'] 