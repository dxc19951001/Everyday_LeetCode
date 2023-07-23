# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 704.二分查找.py 关联题目33
    @date：2022/12/22 0:15
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 设置一个左闭右闭的区间
        left = 0
        right = len(nums)-1

        # 因为是左闭右闭的区间left可以等于right，所以要<=
        while left <= right:
            # 找到这个区间的中间索引
            mid = (left+right)//2
            # 如果中间索引位置的值大于target
            if nums[mid] > target:
                # 则右边指针指向mid-1位置
                # 因为mid的位置已经判断过了
                right = mid -1
            # 如果中间索引位置的值大于target
            elif nums[mid] < target:
                # 则左边指针指向mid+1位置
                # 因为mid的位置已经判断过了
                left = mid + 1
            # 最后返回mid，即target的值
            else:
                return mid
        # 如果没有找到返回-1
        return -1