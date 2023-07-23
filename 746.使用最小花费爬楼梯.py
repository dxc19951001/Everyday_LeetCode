# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 746.使用最小花费爬楼梯.py
    @date：2022/12/24 23:29
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 核心思想：动态规划
        # 确定dp[i]的含义，从第i个台阶出发所要花费的体力
        # 确定动态转移方程：
        #   因为一次能向上爬1个台阶或者1个台阶
        #   所以当前层只能从i-1或者i-2的台阶跳上来
        #   题目要求是最小的体力，所以为min(dp[i - 1], dp[i - 2])
        #   再根据我们dp[i]的定义，要从i个台阶出发，所以要加上第i个台阶的体力
        #   最终动态转移方程为： dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        # 注意：
        #   题目要求爬到顶峰，隐藏含义是要超过最大台阶，即最大台阶数+1
        #   所以要再cost台阶数组中添加上这个隐藏的顶峰，顶峰所花费的体力值是0
        # 初始条件：
        #   即 dp[0] = cost[0]  dp[1] = cost[1]

        if len(cost) <= 1:
            return min(cost[0], cost[1])

        cost.append(0)
        n = len(cost)
        dp = [0 for i in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return dp[-1]
