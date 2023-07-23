# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 463.岛屿的周长.py 关联题目200 695
    @date：2022/12/21 22:49
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 岛屿问题采用递归解决
        # 反向思维
        # 如果边界情况是 海 或者是 外围 会提供一条边界
        # 如果边界情况是已经遍历过的岛屿的话则不提供边界

        def dfs(grid, i, j):
            # 是外围的边界情况
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]):
                return 1
            # 是海的边界情况
            if grid[i][j] == 0:
                return 1
            # 是已经遍历过的岛屿的情况
            if grid[i][j] == 2:
                return 0
            # 设置已遍历过的状态
            grid[i][j] = 2

            return dfs(grid, i + 1, j) + dfs(grid, i, j + 1) + dfs(grid, i - 1, j) + dfs(grid, i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(grid, i, j)
