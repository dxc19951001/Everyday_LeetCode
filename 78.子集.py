# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 78.子集.py
    @date：2023/1/6 0:42
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 核心思想：回溯
        # 回溯参数：nums、循环开始下标startindex
        # 回溯终止条件：当startindex为len(nums)时
        # 回溯搜索遍历：
        #   从startindex开始循环到n，左闭右闭区间
        #   每次节点加入到path中
        #   递归循环，每次startindex向后移一位
        #   到i循环完成后回溯，去掉当前的i进入到i+1

        path = []
        res = []

        def backtrack(nums, startindex):
            res.append(path[:])

            if startindex == len(nums):
                return

            for i in range(startindex, len(nums)):
                path.append(nums[i])
                backtrack(nums, i + 1)
                path.pop()

        backtrack(nums, 0)

        return res
