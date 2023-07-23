# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 134.加油站.py
    @date：2023/1/10 15:35
"""


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 贪心算法
        # 1.如果sum(gas) < sum(cost)，说明加油满足不了消耗，所以无法跑完一圈
        # 2.为了跑完一圈，则再前往一个加油站时要有油
        #   所以cur_sum += gas[i] - cost[i]，必须一直为正数
        #   若出现负数则表示无法跑到下一个加油站
        #   题目说明有唯一的解，所以当cur_sum一直大于0的起始点，就为出发点

        if sum(gas) < sum(cost):
            return -1

        start = 0
        cur_sum = 0
        for i in range(len(gas)):
            print(gas[i] - cost[i])
            cur_sum += gas[i] - cost[i]
            print("cur sun", cur_sum)
            if cur_sum < 0:
                cur_sum = 0
                start = i + 1

        return start