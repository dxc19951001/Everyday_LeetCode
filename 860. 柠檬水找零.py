# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 860. 柠檬水找零.py
    @date：2023/1/10 16:12
"""


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # 贪心算法
        # 根据题目要求写不同的分支

        change_5 = 0
        change_10 = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                change_5 += 1
            elif bills[i] == 10 and change_5:
                change_10 += 1
                change_5 -= 1
            elif bills[i] == 20 and change_5 and change_10:
                change_10 -= 1
                change_5 -= 1
            elif bills[i] == 20 and change_5 >= 3:
                change_5 -= 3
            else:
                return False

        return True