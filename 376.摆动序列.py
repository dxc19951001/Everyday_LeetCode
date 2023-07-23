# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 376.摆动序列.py
    @date：2023/1/9 16:07
"""


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 找到单调递增和单调递减的极值点
        # 各个极值的个数和就是，最长子序列
        # pre_diff表示当前数与前一个数的差值
        # nexe_diff表示当前数与下一个数的差值
        # next_diff * pre_diff 为负数，表示为极值点
        # 为了从偷开始计算pre_diff设置为0
        # 所以满足next_diff * pre_diff <= 0 并且next_diff != 0

        pre_diff, next_diff, res = 0, 0, 1
        for i in range(len(nums) - 1):
            next_diff = nums[i + 1] - nums[i]
            if next_diff * pre_diff <= 0 and next_diff != 0:
                res += 1
                pre_diff = next_diff

        return res