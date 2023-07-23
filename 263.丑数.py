# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 263.丑数.py
    @date：2023/1/13 23:15
"""

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 用n依次除以2，5，5
        # 如果n==1，则表明因数只有2，3，5；否则表明有其他因数

        if n == 0:
            return False

        nums = [2, 3, 5]
        for i in nums:
            while n % i == 0:
                n = n // i
        return n == 1
