# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 1813.句子相似性 III.py
    @date：2023/1/16 1:33
"""


class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        # 判断两个句子第一个和最后一个是否相等
        # 如果相等就同时去掉
        # 如果其中有一个到最后为空了，则表明在中间可以插入句子使得两个句子相等

        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")

        while s1 and s2:
            if s1[0] == s2[0]:
                s1.pop(0)
                s2.pop(0)
            elif s1[-1] == s2[-1]:
                s1.pop()
                s2.pop()
            else:
                return False
        return not s1 or not s2
