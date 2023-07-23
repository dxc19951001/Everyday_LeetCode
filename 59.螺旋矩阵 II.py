# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 59.螺旋矩阵 II.py
    @date：2023/1/3 0:00
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 核心思想：依次循环四条边，每条边都是左闭右开
        # 正整数n的螺旋数组，要循环n//2次，记作loop
        # 依次循环每条边
        # 记每次循环的偏移量为offset，取指范围为[1,loop+1),左闭右开
        #   因为数组为n*n，数组中的元素下标为n-1 * n-1
        # 依次循环四条边

        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0
        loop, mid = n//2, n//2
        count = 1

        for offset in range(1, loop+1):
            # 从左到右
            # x不变为startx，y发生变化从startx到n-offset
            for i in range(startx, n-offset):
                nums[startx][i] = count
                count += 1
            # 从上到下
            # x发生变化从starty到n-offset，y不变为n-offset
            for i in range(starty, n-offset):
                nums[i][n-offset] = count
                count += 1
            # 从右到左
            # x不变为n-offset，y发生变化从n-offset到startx
            for i in range(n-offset, startx, -1):
                nums[n-offset][i] = count
                count += 1
            # 从下到上
            # x发生变化从n-offset到starty，y不变为starty
            for i in range(n-offset, starty, -1):
                nums[i][starty] = count
                count += 1
            # 循环一层后，开始坐标向里层循环
            startx += 1
            starty += 1

        # 如果时奇数，则数组中举数字为n的平方
        if n % 2 != 0:
            nums[mid][mid] = n**2

        return nums

    def generateMatrix2(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 参照54题
        rows, columns = n, n
        res = [[0] * n for _ in range(n)]
        count = 1
        left, right, top, bottom = 0, columns - 1, 0, rows - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res[top][i] = count
                count += 1
            for i in range(top + 1, bottom + 1):
                res[i][right] = count
                count += 1
            if left < right and top < bottom:
                for i in range(right - 1, left, -1):
                    res[bottom][i] = count
                    count += 1
                for i in range(bottom, top, -1):
                    res[left][i] = i
                    count += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return res

