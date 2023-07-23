# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 47.全排列 II.py
    @date：2023/1/6 0:15
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 核心思想
        # 每次循环需要减枝

        path = []
        res = []
        used = [0] * len(nums)  # used列表：判断该元素有没有被使用过，0-没有使用；1-使用过了

        def backtracking(nums, used):
            # 终止条件
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                # 减枝条件：被使用过的元素下次不能使用
                if used[i] == 0:
                    # 剪枝条件 2
                    # 从第二元素开始
                    # 当前元素和前一个元素相同，且前一个元素未使用过
                    # 表明在一层中当前元素重复读取了
                    if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
                        continue
                    used[i] = 1
                    path.append(nums[i])
                    backtracking(nums, used)
                    path.pop()
                    used[i] = 0

        # 记得给nums排序
        backtracking(sorted(nums), used)

        return res