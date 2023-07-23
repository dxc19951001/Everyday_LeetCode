# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 55.跳跃游戏.py
    @date：2023/1/9 17:50
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 每到一个点，将该点之后的num[i]长度的dp变成true
        if len(nums) == 1:
            return True

        dp = [False] * len(nums)
        dp[0] = True

        for i in range(len(nums) - 1):
            if dp[i]:
                if i + 1 + nums[i] > len(nums):
                    return True
                dp[i + 1: i + nums[i] + 1] = [True] * nums[i]

        return dp[-1]

    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 贪心算，计算每一个下标所能覆盖的最大范围
        # 在最大范围内的每一个元素都可进行跳转，更新最大范围
        if len(nums) == 1:
            return True

        cover = 0
        for i in range(len(nums) - 1):
            if i <= cover:
                cover = max(cover, nums[i] + i)
                if cover >= len(nums) - 1:
                    return True

        return False