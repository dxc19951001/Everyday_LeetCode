# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 62.不同路径.py
    @date：2022/12/25 0:07
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 核心思想：动态规划
        # 确定dp[i][j]的含义：到达[i][j]坐标时的方法数
        # 确定动态转移方程：
        #   题目说只能向下或则向右移动，所以坐标[i][j]只能从[i][j - 1]和[i - 1][j]走来出来
        #   所以到达[i][j]的方法是[i][j - 1]和[i - 1][j]方法的和
        #   即dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # 初始条件：
        #   dp[0][1]和dp[1][0]只有一种方法走来，所以为1

        # dp = [[1 for i in range(n)] for j in range(m)]
        dp = [[1] * n for _ in range(m)]  # 设置为1是因为最上边和最左边的格子都只有1种方法能到达

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
