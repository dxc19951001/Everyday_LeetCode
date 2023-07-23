# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 518.零钱兑换 II.py
    @date：2022/12/27 23:10
"""


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # 核心思想：动态规划（完全背包)
        # 背包容量为amount，物品价值为coins[i]，重量为coins[i]
        # 完全背包循环为先物品，再背包，正序循环
        # 求组合动态转移方程为dp[j] += dp[j - coins[i]]

        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]

        return dp[-1]