# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 18.四数之和.py
    @date：2023/1/2 22:26
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 核心思想：双指针
        # 两层循环表示数字a和b，再内部使用双指针，参考第15题

        nums.sort()
        ans = []

        for i in range(len(nums)):
            # 去重重复a
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                # 去除重复b
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                rigth = len(nums) - 1
                while left < rigth:
                    total = nums[i] + nums[j] + nums[left] + nums[rigth]
                    if total < target:
                        left += 1
                    elif total > target:
                        rigth -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[rigth]])
                        while left < rigth and nums[left] == nums[left + 1]:
                            # 去重数字c
                            left += 1
                        while left < rigth and nums[rigth] == nums[rigth - 1]:
                            # 去重数字d
                            rigth -= 1
                        left += 1
                        rigth -= 1

        return ans