# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 387.字符串中的第一个唯一字符.py
    @date：2023/1/13 23:52
"""
from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 统计s中的每个字符的个数，找到第一个个数为1的字母的下标
        hash_s = Counter(s)

        for i in range(len(s)):
            if hash_s[s[i]] == 1:
                return i
        return -1
