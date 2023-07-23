# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 90.子集 II.py
    @date：2023/1/6 0:52
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 参考第第78题
        # 注意:需要增加去重逻辑：
        # if i > startindex and nums[i] == nums[i - 1]:
        #   continue

        path = []
        res = []

        def backtrack(nums, startindex):
            res.append(path[:])

            if startindex == len(nums):
                return

            for i in range(startindex, len(nums)):
                if i > startindex and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(nums, i + 1)
                path.pop()

        backtrack(sorted(nums), 0)

        return res
