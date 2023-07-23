# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 56.合并区间.py
    @date：2023/1/12 0:43
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 贪心算法
        # 按照右边范围进行排序
        # 将intervals中的元素放入result列表中
        # 如果放入的元素的左边区间 小于等于 result中最后一个元素的右边区间，则为重叠区间，进行合并
        # 否则就直接加入到result列表中

        intervals.sort(key=lambda x: x[0])
        result = [intervals.pop(0)]
        i = 0
        while intervals:
            tmp = intervals.pop(0)
            if result[i][1] >= tmp[0]:
                result[i][1] = max(result[i][1], tmp[1])
            else:
                result.append(tmp)
                i += 1

        return result
