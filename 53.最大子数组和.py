# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 53.最大子数组和.py
    @date：2023/1/4 2:28
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i]前i个连续数字的和
        # 动态转移方程：
        #   如果连续到第i个数字和为dp[i - 1] + nums[i]
        #   如果不连续第i个数字，则为nums[i]
        #   所以方程为max(dp[i - 1] + nums[i], nums[i])
        # 返回dp中嘴的数

        if not nums:
            return nums

        dp = [0] * len(nums)
        result = dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            result = max(dp[i], result)

        return result