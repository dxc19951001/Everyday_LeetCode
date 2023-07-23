# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 159.至多包含两个不同字符的最长子串.py
    @date：2022/12/20 1:17
"""

"""
给你一个字符串 s ，请你找出至多包含 两个不同字符 的最长子串，并返回该子串的长度。


示例 1：
输入：s = "eceba"
输出：3
解释：满足题目要求的子串是 "ece" ，长度为 3 。

示例 2：
输入：s = "ccaabbb"
输出：5
解释：满足题目要求的子串是 "aabbb" ，长度为 5 。


提示：
1 <= s.length <= 105
s 由英文字母组成

"""


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 定义length记录最大长度
        # 定义 queue 为滑动窗口

        length = 0
        queue = []

        for i in s:
            queue.append(i)  # 向滑动窗口中增加元素
            cont = set(queue)  # 使用set去重，来确定元素的个数
            if len(cont) > 2:  # 如果元素种类超过两个
                # 记录此时的最大字符串长度
                # 因为是加了一个元素之后，此时有3个元素种类，所以要把多的减掉即len(queue) - 1
                length = max(length, len(queue) - 1)
                while len(cont) > 2:
                    # 从queue头开始删除元素直至元素种类为2个
                    queue.pop(0)
                    cont = set(queue)

        # 如果字符串始终没有超过两种
        # 则执行不到if语句中，直接输出len(queue）
        return max(length, len(queue))
