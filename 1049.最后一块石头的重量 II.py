# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 1049.最后一块石头的重量 II.py
    @date：2022/12/25 22:34
"""


class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # 核心思想：动态规划（背包问题）
        # 如果想要返回此石头重量最小，可以将石头分成两份，每份的重量为 sum(stones)//2
        # 如果想要装的下 sum(stones)//2 重量的石头，就需要容积为 sum(stones)//2 的背包
        # 因此问题转换成背包容积为sum(stones)//2，商品重量为stones[i]，商品价值为stones[i]
        # 此时背包所能装的最大价值物品的问题，即0-1背包问题
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
        # 当容量为sum(nums)//2的背包装满后，为dp[j]
        # 剩下另一半的最大重量为 sum(nums)//2 - dp[j]
        # 两堆的差值为 sum(nums)//2 - dp[j] - dp[j]，即为所求的最小值

        sumweight = sum(stones)
        target = sumweight // 2
        dp = [0] * (target + 1)
        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])

        return sumweight - 2 * dp[target]
