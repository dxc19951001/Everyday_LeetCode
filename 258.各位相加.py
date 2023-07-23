# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 258.各位相加.py
    @date：2023/1/13 23:01
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 模拟个各个位置数相加的过程
        sum = num
        while sum // 10:
            tmp = 0
            while num:
                tmp += num % 10
                num = num//10
            sum = num = tmp
        return sum
