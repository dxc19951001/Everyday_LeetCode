# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 494.目标和.py
    @date：2022/12/26 23:09
"""

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 核心思想：动态规划（背包问题）
        # 要得到目标target可将数组中数分成left和right两部分，left为相加部分，right为相减部分
        # sum(nums) = right + left
        # target = left - right
        # 所以target = left - (sum(nums) -left)  即 left = (sum(nums) + target)/2
        # 因此可以转换成当背包容积为left = (sum(nums) + target)/2 ，物品价值为nums[i],物品重量为nums[i]，放入背包有多少种方法
        #
        # dp[j]含义：容量为j的背包有dp[j]种方法可以放满
        # 动态转移方程：
        #   放入i物品后，背包剩余容量为j - nums[i]，根据dp定义，j - nums[i]容量的背包有dp[j - nums[i]]种方法
        #   每一个物品都放入背包中后，再将所对应的方法相加，即为背包容量为j时所能方满的方法数
        # 初始化：dp[0]等于1，因为需要从容量为0处向后推到

        sumValue = sum(nums)

        # 边界场景：
        #   1.目标值大于nums总和；
        #   2.由于题目要求为非负整数，left = (sum(nums) + target)/2
        #     所以(sum(nums) + target)必须为非负偶数，left才能是非负整数
        if abs(target) > sumValue or (sumValue + target) % 2 == 1:
            return 0
        bagSize = (sumValue + target) // 2
        dp = [0] * (bagSize + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagSize, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[bagSize]
