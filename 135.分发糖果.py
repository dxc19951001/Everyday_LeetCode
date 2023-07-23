# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 135.分发糖果.py
    @date：2023/1/10 15:53
"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # 贪心算法
        # 先算左边的孩子比右边孩子大的情况
        # 再算右边孩子比左边孩子大的情况

        res = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)  # 因为要比左边和右边都大，取左边和右边的最大值

        return sum(res)