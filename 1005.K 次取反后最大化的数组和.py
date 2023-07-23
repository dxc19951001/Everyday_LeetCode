# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 1005.K 次取反后最大化的数组和.py
    @date：2023/1/10 14:49
"""


class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 贪心算法
        # 排序nums将所以负数变成正数
        # 如果k还有剩余，则将新的nums排序
        # k为奇数nums中最小的数取负，k为偶数无需处理

        nums.sort()
        for i in range(len(nums)):
            if nums[i] <= 0 and k > 0:
                nums[i] = - nums[i]
                k -= 1
            elif nums[i] > 0:
                # 如果都是正数了就退出循环
                break

        nums.sort()
        if k > 0:
            if k % 2 == 1:
                nums[0] = - nums[0]

        return sum(nums)