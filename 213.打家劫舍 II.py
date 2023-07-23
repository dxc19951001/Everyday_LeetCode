# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 213.打家劫舍 II.py
    @date：2022/12/28 17:22
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 核心思想：动态规划
        # 参考第198题
        # 不同之处，本题需要分两种情况讨论
        #   1.偷第1间房，不偷最后一间房
        #   2.偷第最后一间房，不偷第一间房
        # 分别对两种情况进行求解，两种情况中最大的情况为本题的解


        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        # 偷第一间房
        tmp1 = nums[:-1]
        dp = [0] * len(tmp1)
        dp[0] = tmp1[0]
        dp[1] = max(tmp1[0], tmp1[1])

        for i in range(2, len(tmp1)):
            dp[i] = max(dp[i - 1], dp[i - 2] + tmp1[i])

        # 偷第n间房
        tmp2 = nums[1:]
        bp = [0] * len(tmp2)
        bp[0] = tmp2[0]
        bp[1] = max(tmp2[0], tmp2[1])

        for i in range(2, len(tmp2)):
            bp[i] = max(bp[i - 1], bp[i - 2] + tmp2[i])

        return max(dp[-1], bp[-1])
