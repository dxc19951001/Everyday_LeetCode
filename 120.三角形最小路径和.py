from typing import List


class Solution:
    def minimumTotal1(self, triangle):

        # 核心思想
        # 从上往下，从最底部元素向上求解
        # 比较下一行相邻两个值triangle[i][j]和triangle[i][j + 1]
        # 较小的值与上一行triangle[i - 1][j]相加，得到[i - 1][j]位置到最底部元素的最小值
        # triangle[i - 1][j] += min(triangle[i][j], triangle[i][j + 1])
        # 示例
        # [
        #     [2],
        #     [3,4],
        #     [6,5,7],
        #     [4,1,8,3]
        # ]
        # 通过观察三角形可以看出，第一行有1个元素，第二行有两个元素，第三行有三个元素......
        # 且上一行比下一行元素少一个

        for i in range(len(triangle) - 1, 0, -1):
            # 从下往上遍历，i==每一行元素个数-1
            # 遍历到第二行为止
            for j in range(i):
                # 由于上一行比下一行元素少一个，所以j正好为上衣行元素个数
                # 而triangle[i][j + 1]正好可以最终取到本行的最后一个元素
                triangle[i - 1][j] += min(triangle[i][j], triangle[i][j + 1])
        return triangle[0][0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # 核心思想
        # 自上而下
        # dp[i][j]为(i, j)点到底边的最小路径和，
        # 则动态转移方程为：dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
        # n = len(triangle)
        # 构建一个n*n，值都为float('inf')的dp数组
        # 初始条件:dp[0][0] = triangle[0][0]

        dp = [[float('inf')] * len(triangle) for _ in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(i+1):
                # 每一行的元素个数j，比行数大1
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        return min(dp[-1])
