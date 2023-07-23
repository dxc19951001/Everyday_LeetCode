# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 33.搜索旋转排序数组.py
    @date：2022/12/22 2:07
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 先找到分割线,即从左往右第一个小于nums[0]的数的索引
        # 该索引即为分割点
        # 分割点之前的数 都比 分割点之后的数大
        # 且两部的数据都从大到小排列
        start = 1
        gap = end = len(nums) - 1
        while start <= end:
            if nums[start] < nums[0]:
                gap = start
                break
            start += 1

        # 如给第0个数等于 target 直接返回
        if nums[0] == target:
            return 0
        # 如果第0个数大于target，则target在后半部分
        elif nums[0] > target:
            # 在后半部分进行二分查找
            # 注意：
            # 1.返回值要加上直接的分割点索引，才是真正的在nums中的索引值
            # 2.若在在后半部部分没有找到返回-1，不能直接加分割点索引，要直接返回-1
            if self.binary_search(nums[gap:], target) != -1:
                return self.binary_search(nums[gap:], target) + gap
            else:
                return -1
        # 如果第0个数小于target，则target在前半部分
        # 在前半部分直接返回找到的索引值即可，因为前半部分索引值与nums索引相等
        else:
            return self.binary_search(nums[0:gap+1], target)

    # 封装一个二分查找方法
    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

