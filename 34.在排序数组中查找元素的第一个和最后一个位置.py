# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 34.在排序数组中查找元素的第一个和最后一个位置.py
    @date：2023/1/19 0:40
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 核心思想 二分查找
        # 找到nums中的第一个target值
        # 再找到第一个比target值大1的数，该数的下标减1就是最后一个target数
        if not nums:
            return [-1, -1]

        def search(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right-left) // 2
                if nums[mid] >= target:
                    right = mid -1
                else:
                    left = mid + 1
            return left

        left_index = search(nums, target)
        right_index = search(nums, target+1) -1

        # left_index可能超出索引限制，例如nums=[2,2]  target=3
        # nums[left_index]没有找到目标值
        if left_index > len(nums) -1 or nums[left_index] != target:
            return [-1, -1]

        return [left_index, right_index]