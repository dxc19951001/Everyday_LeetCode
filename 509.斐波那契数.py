# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 509.斐波那契数.py
    @date：2022/12/24 14:21
"""


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 核心思想：动态规划

        if n == 0:
            return 0

        dp = [0 for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # print(dp)
        return dp[-1]