# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 1807.替换字符串中的括号内容.py
    @date：2023/1/12 1:06
"""


class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        # 将knowledge转换为字典
        # 循环得到()号内的内容，将其替换成字典对应的内容

        knowledge = dict(knowledge)
        ans = []
        start = -1
        for i in range(len(s)):
            if s[i] == "(":
                start = i
            elif s[i] == ")":
                ans.append(knowledge.get(s[start + 1: i], "?"))
                start = -1
            elif start == -1:
                ans.append(s[i])

        return "".join(ans)
