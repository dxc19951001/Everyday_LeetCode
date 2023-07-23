from typing import List


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 核心思想：动态规划
        # 确定dp[i][j]的含义：到达[i][j]坐标时的方法数
        # 确定动态转移方程：
        #   参考第63题，为dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # 初始条件：
        #   初始dp数组都设置为0
        #   当obstacleGrid[0][0] == 0，则直接返回0，开始就有障碍物
        #   循环判断obstacleGrid的第一行是否存在障碍物
        #       不存在障碍物则设置为1；若存在障碍物则从障碍物点往后都是0
        #   循环判断obstacleGrid的第一列是否存在障碍物
        #       不存在障碍物则设置为1；若存在障碍物则从障碍物点往后都是0
        # 遍历dp：
        #   当obstacleGrid[i][j] != 1 时，用动态转移方程计算dp[i][j]
        #   当obstacleGrid[i][j] == 1 时，当前点不可到达，即为0

        n = len(obstacleGrid[0])
        m = len(obstacleGrid)

        dp = [[0] * n for _ in range(m)]

        # 判断开始点
        dp[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        if dp[0][0] == 0:
            return 0

        # 判断第一行
        for k in range(n):
            if obstacleGrid[0][k] == 1:
                break
            dp[0][k] = 1

        # 判断第一列
        for l in range(m):
            if obstacleGrid[l][0] == 1:
                break
            dp[l][0] = 1

        # 用动态转移方程计算dp
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]