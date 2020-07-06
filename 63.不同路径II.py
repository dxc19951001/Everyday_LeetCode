from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # 核心思想
        # 动态规划
        # n = len(obstacleGrid)+1 ; m = len(obstacleGrid[0])+1
        # 加1，是增加dp初始状态的行和列
        # 构建一个n*m的全零dp二维数组
        # 每个dp格子相当于可以走到的路径数
        
        # 开始是从dp[1][1]出发，所以走到dp[1][1]必然有一种方法
        # 所以dp[1][1]=1
        
        # 走到每一个格子dp[i][j]的方式，只能从左边和上方走到
        # 因此走到该格子的路径数=走到左边的路径数+走到上方的路径数
        # 因此递推公式：dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # 考虑到obstacleGrid中有障碍，有障碍的地方无法走通，路径数为0
        # 所以当obstacleGrid中数值为1的地方，dp值为0

        # 特殊情况
        # obstacleGrid[0][0] == 1，说明一开始位置就有障碍物，根本无法行走，直接返回0

        # 最终放回dp中最后一个值dp[-1][-1]即为答案

        n = len(obstacleGrid)+1  # 行
        m = len(obstacleGrid[0])+1  # 列
        dp = [[0]*m for _ in range(n)] # dp为n*m

        if obstacleGrid[0][0] == 1:
            # 一开始就有障碍物，没法走，直接返回0
            return 0

        # 注意i和j是dp数组的索引不是obstacleGrid的索引
        # i-1和j-1才是obstacleGrid中的索引
        for i in range(1, n):
            # i代表行
            for j in range(1, m):
                # j代表列
                if i == 1 and j == 1:
                    # 从dp[1][1]出发，数据数为1
                    dp[1][1] = 1
                elif obstacleGrid[i-1][j-1] == 1:
                    # 遇到障碍，dp数值为0
                    dp[i][j] = 0
                else:
                    # 普通情况下，为左边的路径数+右边的路径数
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
       
        return dp[-1][-1]