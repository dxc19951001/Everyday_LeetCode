# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 27.移除元素.py
    @date：2022/12/28 1:30
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 同样使用双指针方案

        if not nums:
            return 0

        nums_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[nums_index] = nums[i]
                nums_index += 1

        return nums_index