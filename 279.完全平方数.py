# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 279.完全平方数.py
    @date：2022/12/28 0:18
"""


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 参考第322题
        # 初始化物品的列表，列表中元素比n要小
        nums = [i ** 2 for i in range(1, n + 1) if i ** 2 <= n]

        dp = [n + 1] * (n + 1)
        dp[0] = 0

        for i in range(len(nums)):
            for j in range(nums[i], n + 1):
                dp[j] = min(dp[j], dp[j - nums[i]] + 1)

        return dp[-1]