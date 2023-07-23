# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 452.用最少数量的箭引爆气球.py
    @date：2023/1/10 17:22
"""


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 贪心算法
        # 先安装左范围的大小进行排序，如果相同再按照右范围大小进行排序
        # 1.第i个元素的左范围 大于 第i-1个元素的右边范围，则说明这两个元素不重回，则需要一支键
        # 2.第i个元素的左范围 小于等于 第i-1个元素的右边范围，则说明两个元素重合
        #   需要确定重合部分的右边范围，右边范围时第i个和第i-1个元素右边范围的最小值
        #   将其作为第i个元素新的右边范围，参加下一次计算

        points.sort(key=lambda x: (x[0], x[1]))

        count = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]:
                count += 1
            else:
                points[i][1] = min(points[i - 1][1], points[i][1])

        return count