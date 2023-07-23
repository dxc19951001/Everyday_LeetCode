# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 26.删除有序数组中的重复项.py
    @date：2022/12/28 1:21
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 核心思想：通过双指针的方法，比较强前后两个元素是否相等，如果不相等就将该元素放到前面去

        if not nums:
            return 0

        # 初始化不重复元素的数量
        num_unique = 1

        # 遍历数组中的所有元素
        for i in range(1, len(nums)):
            # 如果当前元素与前一个元素不同，就将它添加到不重复元素的数量中
            if nums[i] != nums[i - 1]:
                nums[num_unique] = nums[i]
                num_unique += 1
        return num_unique