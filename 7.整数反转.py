# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 7.整数反转.py
    @date：2023/1/12 16:15
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = 1 if x > 0 else -1
        x = abs(x)

        res = 0
        while x:
            res = x % 10 + res * 10
            x = x//10

        res = res*n

        if -2**31 <= res <= 2**31-1:
            return res
        else:
            return 0
