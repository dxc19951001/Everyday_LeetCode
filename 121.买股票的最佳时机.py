# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 121.买股票的最佳时机.py
    @date：2022/12/19 23:10
"""
from typing import Any

class Solution(object):

    # 暴力解法，以当前的日期价格后后面的日期价格做比较
    def maxProfit(self, prices: Any) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                ans = max(ans, prices[j] - prices[i])

        return ans

    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 从后往前，依次记录最小的数
        # 因为我们想要在最小的时候买进，最高的时候卖出
        # 计算最小数后面的数与最小数的差值，找出最大的即为结果
        # 最小数在会发生变化，因此需要记录最小数

        # 当前天的数值，减去前面天中数值最小的，即为当前天的最大利润

        minprice = prices[0]  # 假设第一个数时最小数
        maxprofit = 0  # 记录最大利润，最大利润默认为0
        for price in prices:
            # 当前数减去最小数为赚取的最大利润
            # 与记录的最大利润进行比较，取最大值
            maxprofit = max(price - minprice, maxprofit)
            # 若当前数比记录的最小数小，则更新该数
            minprice = min(price, minprice)
        return maxprofit

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i]是第i天卖出，所能得到最大利润值
        # 贪心算法：
        #   第i天不卖，则最大利润为i-1天的利润，即dp[i-1]
        #   第i天卖，则最大利润为当天的价格减去前面价格的最小值即prices[i] - minPrice
        #   取两种情况的最大值：dp[i] = max(dp[i - 1], prices[i] - minPrice)


        dp, minPrice = [0] * len(prices), prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])  # 最小价格随着天数的增加实时更新
        return dp[-1]

    def maxProfit3(self, prices):
        # 核心思想：动态规划
        # 确定dp含义
        #   dp[i][0] 表示第i天持有股票所得最多现金
        #   dp[i][1] 表示第i天不持有股票所得最多现金
        # 确定动态转移方程：
        #   如果第i天持有股票即dp[i][0]， 那么可以由两个状态推出来
        #       第i-1天就持有股票，那么就保持现状，所得现金就是昨天持有股票的所得现金 即：dp[i - 1][0]
        #       第i天买入股票，所得现金就是买入今天的股票后所得现金即：-prices[i]
        #       那么dp[i][0]应该选所得现金最大的，所以dp[i][0] = max(dp[i - 1][0], -prices[i]);
        #   如果第i天不持有股票即dp[i][1]， 也可以由两个状态推出来
        #       第i-1天就不持有股票，那么就保持现状，所得现金就是昨天不持有股票的所得现金 即：dp[i - 1][1]
        #       第i天卖出股票，所得现金就是按照今天股票佳价格卖出后所得现金即：prices[i] + dp[i - 1][0]
        #       dp[i][1]取最大的，dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0]);
        # 初始化：
        #   dp[0][0]
        #       表示第0天持有股票，此时的持有股票就一定是买入股票了，因为不可能有前一天推出来，所以dp[0][0] -= prices[0];
        #   dp[0][1]
        #       表示第0天不持有股票，不持有股票那么现金就是0，所以dp[0][1] = 0;

        length = len(prices)
        if length == 0:
            return 0
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])
        return dp[-1][1]  # 返回股票卖出的情况