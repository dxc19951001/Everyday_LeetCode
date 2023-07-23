# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 416.分割等和子集.py
    @date：2022/12/25 17:20
"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 核心思想：动态规划（将题目抽象成背包问题）
        # 背包最容量为：sum(nums)//2
        #   因为背包里物品重量的总和要等于sum(nums)//2
        # 物品的价值为nums[i]，物品重量为nums[i]
        # dp[j]：表示容量为j的背包的最大价值
        # 动态转移方程：
        #   背包里所能得到的最大值为背包在第`i-1`个时物品时的最大值+第i个物品的值，
        #   为了容量`j`能装的下第`i`个物品，背包只能从在装第`i-1`个物品后容量还剩`j-weight[i]`处的地方得到
        #   所以递推公示为`d[j]=[j-weight[i]+value[i]`
        #   最终最大值为`dp[j] = max(dp[j], dp[j - weight[i]] + value[i])`
        # 初始化：
        #   未放置物品时都取0
        # 循环顺序：
        #   先循环物品再循环背包，从后向前循环，因为每一个元素只能取一次
        # 当容量为sum(nums)//2装满后判断其装的物品最大价值是否为为sum(nums)//2，时就返回True

        target = sum(nums)
        if target % 2 == 1:
            # 如果和为奇数，不存在两个子集相等的情况
            return False
        target //= 2
        dp = [0] * (target + 1)
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        return dp[target] == target
