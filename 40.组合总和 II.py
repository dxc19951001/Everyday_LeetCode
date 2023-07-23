# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 40.组合总和 II.py
    @date：2023/1/3 23:28
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 与第39题类似
        # 区别：因为candidates存在重复元素，需要去重
        # 注意：先要对元素进行排序

        res = []
        sum_ = []
        candidates.sort()

        def backtrack(candidates, target, startindex):
            if sum(sum_) == target:
                res.append(sum_[:])
                return

            if sum(sum_) > target:
                return

            for i in range(startindex, len(candidates)):
                # 当前元素与前一个元素相同，则跳过当元素
                # 因为这个元素在上一此已经使用过了
                if i > startindex and candidates[i] == candidates[i - 1]:
                    continue

                sum_.append(candidates[i])
                backtrack(candidates, target, i + 1)
                sum_.pop()

        backtrack(candidates, target, 0)
        return res
