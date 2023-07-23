# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 3.无重复字符的最长子串.py
    @date：2022/12/20 0:31
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 维护一个队列queue，如果字符串中的数不在队列中就将队列中的数加到列表中
        # 若出现列表中循环的数，
        # 1.记录当前列表的长度，并于之前的最大长度比较
        # 2.删除列表中第一个元素，直至无重复的元素


        length = 0  #记录最大长度

        queue = []
        for i in s:
            if i in queue:
                length = max(length, len(queue))
                while i in queue:
                    queue.pop(0)

            queue.append(i)

        # 如果字符串始终没有重复的化
        # 则执行不到if语句中，直接输出len(queue）
        return max(length, len(queue))


    # 给定一个字符串，请你找出其中不含有重复字符的最长子串
    # 输入：aadeffdffc ->adef
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """

        queue = ""
        res = ""

        for i in s:
            if i in queue:
                res = queue if len(queue) > len(res) else res
                while i in queue:
                    queue = queue[1:]
            queue += i

        return max(res, queue)
