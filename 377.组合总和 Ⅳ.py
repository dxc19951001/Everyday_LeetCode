# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 377.组合总和 Ⅳ.py
    @date：2022/12/27 23:32
"""


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 核心思想：动态规划
        # 1. 如果求组合数就是外层for循环遍历物品，内层for遍历背包。
        # 2. 如果求排列数就是外层for遍历背包，内层for循环遍历物品。
        # 动态转移方程：dp[j] += dp[j - nums[i]]

        dp = [0] * (target + 1)
        dp[0] = 1

        for j in range(target + 1):
            for i in range(len(nums)):
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]

        return dp[-1]
