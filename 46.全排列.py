# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 46.全排列.py
    @date：2023/1/5 14:38
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        res = []

        def backtrack(nums):
            if len(path) == len(nums):
                res.append(path[:])
                return

            # 单层递归逻辑
            for i in range(0, len(nums)):  # 从头开始搜索
                # 若遇到self.path里已收录的元素，跳过
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(nums)
                path.pop()

        backtrack(nums)

        return res