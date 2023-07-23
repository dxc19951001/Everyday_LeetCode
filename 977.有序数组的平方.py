# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 977.有序数组的平方.py
    @date：2023/1/2 22:50
"""

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 核心思想：双指针
        # 创建一个与nums一样大小的数组
        # i指向nums[0]，j指向nums[n-1]
        # k指向新数组的最后一位，每次比较nums[0]和nums[n-1]的平方，数字大的放到新数组的第k位
        n = len(nums)
        i, j, k = 0, n-1, n-1
        ans = [-1] * n
        while i <= j:
            num_i = nums[i] ** 2
            nums_j = nums[j] ** 2
            if num_i > nums_j:
                ans[k] = num_i
                i += 1
            else:
                ans[k] = nums_j
                j -= 1
            k -= 1
        return ans