# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 695.岛屿的最大面积.py 关联题目463 200
    @date：2022/12/21 23:14
"""


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 通过dfs递归的方式找到每一个岛屿的所有'1'
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] != 1:
                return 0
            grid[i][j] = 2  # 设置岛屿找过的状态

            # 返回值为1加之前找到的岛屿'1'，为岛屿的面积
            return 1 + dfs(grid, i + 1, j) + dfs(grid, i, j + 1) + dfs(grid, i - 1, j) + dfs(grid, i, j - 1)

        square = 0  # 记录每次找到的岛屿面积
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    square = max(square, dfs(grid, i, j))
        return square