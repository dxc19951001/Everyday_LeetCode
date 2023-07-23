# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 2287.重排字符形成目标字符串.py
    @date：2023/1/13 13:07
"""
from collections import Counter


class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        # hash后，找到target中的字符串在s中的最小倍数
        hash_target = dict()
        hash_s = dict()
        for i in target:
            hash_s[i] = s.count(i)
            hash_target[i] = target.count(i)

        ans = 1000
        for i in target:
            tmp = hash_s[i] // hash_target[i]
            ans = min(ans, tmp)
        return ans

    def rearrangeCharacters2(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """

        count_s, count_target, ans = Counter(s), Counter(target), 1000
        for i in target:
            tmp = count_s[i] // count_target[i]
            ans = min(ans, tmp)
        return ans
