# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 435.无重叠区间.py
    @date：2023/1/12 0:17
"""


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 贪心算法
        # 找到不重复的区间个数，用总的个数减掉不重复的区间个数
        # 按照左范围进行排序
        # 如果第i个右边区间 大于 等于 前面的左区间，则表明这个两个区间不相交
        # 此时，更新左区间，然后找到一个不相交的区间


        intervals.sort(key=lambda x: x[1])
        count = 1
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]

        return len(intervals) - count
