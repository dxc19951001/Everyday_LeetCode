# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 454.四数相加 II.py
    @date：2023/1/2 21:25
"""


class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        # 核心思想：hash表
        # nums1+ nums2 + nums3 + nums4 = 0
        # 先计算nums1和nums2中的元素和 sum = i + j
        # 并用字典记录，key为和的值，val为和出现的次数
        # 在计算nums3和nums4中的每个元素,如果有0 - l - k为key的在字典中的
        # 则累加每个key出现的次数

        hashmap = dict()
        for i in nums1:
            for j in nums2:
                sum = i + j
                if sum in hashmap:
                    hashmap[sum] += 1
                else:
                    hashmap[sum] = 1

        count = 0
        for k in nums3:
            for l in nums4:
                if 0 - l - k in hashmap:
                    count += hashmap[0 - l - k]

        return count
