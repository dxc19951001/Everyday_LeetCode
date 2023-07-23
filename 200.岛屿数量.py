# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 200.岛屿数量.py 关联题目463 695
    @date：2022/12/21 21:50
"""

# 参考思路:https://leetcode.cn/problems/number-of-islands/solution/dao-yu-lei-wen-ti-de-tong-yong-jie-fa-dfs-bian-li-/
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 状态设置
        # 0 —— 海洋格子
        # 1 —— 陆地格子（未遍历过）
        # 2 —— 陆地格子（已遍历过）

        # 通过DFS递归搜索指定节点上下左右是否为'1'
        # 若为1的，则遍历该点后将其设置为2
        # 递归终止条件
        # 指定节点的坐标超过矩阵边界
        # 指定节点左边为0 或者 2，表示为海洋，或者为已经遍历过
        def dfs(grid, i, j):
            # 递归终止条件
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] != '1':
                return
            # 设置已遍历过的状态
            grid[i][j] = '2'
            # 上下左右递归搜索陆地
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)

        count = 0  #设置记录岛屿的数字
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 如果节点为'1'则进入递归搜索
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1

        return count
