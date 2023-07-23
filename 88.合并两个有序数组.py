# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 88.合并两个有序数组.py
    @date：2023/1/13 0:32
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 双指针

        tmp = []
        i, j = 0, 0

        while i < m or j < n:
            if i == m:
                tmp.append(nums2[j])
                j += 1
            elif j == n:
                tmp.append(nums1[i])
                i += 1
            elif nums1[i] <= nums2[j]:
                tmp.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                tmp.append(nums2[j])
                j += 1
        nums1[:] = tmp

    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 调用函数库

        nums1[m:] = nums2
        nums1.sort()
