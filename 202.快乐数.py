# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 202.快乐数.py
    @date：2023/1/2 21:31
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 核心思想：如果一个数不是快乐数，则一直计算下去，计算的结果会出现重复的数
        # 设定一个hash表记录每次计算得到的结果，如果计算结果出现在hash表里的数，则表示数据计算重复，不是快乐数

        def cal_happy_nums(n):
            sum_ = 0
            while n:
                sum_ += (n % 10) ** 2
                n = n // 10
            return sum_

        seen = set()
        while True:
            n = cal_happy_nums(n)
            if n == 1:
                return True

            if n in seen:
                return False
            else:
                seen.add(n)