# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 647.回文子串.py
    @date：2023/1/2 1:14
"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 核心思想：动态规划
        # dp[i][j]：表示字符串s在区间[i,j]内是否为回文字符串
        # 动态转移方程：
        #   1.s[i] == s[j]，区间内首尾相等，为回文字符串的充分必要条件
        #   2.如果j-i <= 1
        #       j和i下标相等指向同一个元素，为回问字符串
        #       j和i下标相差1，例如aa，也为回文字符串
        #   3.j-i > 1
        #       区间[i,j]要想是回文字符串，则要子区间[i+1][j-1]也要为回文字符串
        # 初始状态：数组都为False
        # 循环顺序：
        #   因为要知道[i+1][j-1]的状态，所以外出循环倒序，内层循环正序
        dp = [[False] * len(s) for _ in range(len(s))]
        res = 0

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j-i <= 1:
                        res += 1
                        dp[i][j] = True
                    elif j-i > 1 and dp[i+1][j-1]:
                        res +=1
                        dp[i][j] = True
        return res
