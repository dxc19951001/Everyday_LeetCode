class Solution:
    def shortestPalindrome(self, s: str) -> str:

        # 核心思想--暴力求解
        # 在s中从后向前循环，找到第一个能与s组成回文传的字符

        n = len(s)
        ans = None
        for i in range(n, -1, -1):
            tmp = s[i:]
            ans = tmp[::-1]+s

            if ans == ans[::-1]:
               return ans 