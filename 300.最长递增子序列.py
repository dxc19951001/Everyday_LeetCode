# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 300.最长递增子序列.py
    @date：2022/12/30 23:42
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 核心思想：动态规划
        # dp[i]：表示以nums[i]结尾得最长子序列长度
        # 动态转移方程：
        #   nums[i]之前的序列为nums[0:i]，记作nums[j]
        #   如果nums[i] > nums[j]
        #   计算每一个dp[j]到nums[i]的最长递增子序列长度，即dp[j]+1，并取最大值
        #   动态转移方程为
        #   if nums[i] > nums[j]:
        #       dp[i] = max(dp[i], dp[j]+1)
        # 初始化：
        #   有数字时最少长度为1，所以全部初始化为1

        if len(nums) <= 1:
            return len(nums)

        dp = [1] * len(nums)
        res = 0

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])
        return res
