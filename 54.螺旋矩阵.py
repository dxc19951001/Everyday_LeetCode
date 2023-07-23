# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 54.螺旋矩阵.py
    @date：2023/1/3 1:01
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 模拟循环的情况
        # 使用左闭右闭区间
        # 注意从左到右，从上到小时，需要保证left < right and top < bottom

        if not matrix:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                order.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                order.append(matrix[i][right])
            if left < right and top < bottom:
                for i in range(right - 1, left, -1):
                    order.append(matrix[bottom][i])
                for i in range(bottom, top, -1):
                    order.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return order