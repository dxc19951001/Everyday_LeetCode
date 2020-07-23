from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # 核心思想
        # 动态规划
        # 构建一个n*m的dp数组， 行：n = len(grid)  列：m =len(grid[0])
        # 初始条件dp[0][0] = grid[0][0]
        # 第一行因为没有上方元素，所以第一行的元素值只能从左边得到
        # 第一列因为没有左方方元素，所以第一列的元素值只能从上边得到
        # 其他元素的值，由上方或左边最小的值得到
        # 最终返回最后一个元素dp[-1][-1]
        
        n = len(grid)  # 行
        m =len(grid[0])  # 列
        
        dp = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                elif i==0 and j>0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j==0 and i>0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]