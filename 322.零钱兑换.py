# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 322.零钱兑换.py
    @date：2022/12/27 23:59
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 核心思想：完全背包
        # dp[j]：凑足总额为j所需钱币的最少个数为dp[j]
        #       装满容量为j的背包最小的物品个数为dp[j]
        # 因为是个个数所以动态转移方程为：min(dp[j], dp[j - weight[i]] + 1)
        # 初始化：dp[0] = 0
        # 非0下标，因为要求最小值为了防止被覆盖，所以要用个极大值，所以用amount + 1
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)

        # 返回时注意，若没有满足的条件dp[amount] == amount + 1，此时因返回-1
        return dp[amount] if dp[amount] < amount + 1 else -1
