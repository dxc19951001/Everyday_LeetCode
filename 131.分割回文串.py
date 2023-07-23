# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 131.分割回文串.py
    @date：2023/1/4 1:58
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # 核心思想：回溯
        # 回溯参数：s，开始分割的下标startindex
        # 递归终止条件：startindex等于len(s)，表示已经切割到最后一个数了
        # 单层循环：循环范围从startindex到len(s))
        #   如果从startindex到i是回文字符串的话，就加入到record中，再继续向下切割，即startindex = i + 1

        if not s:
            return []

        res = []
        record = []

        def backtrack(s, startindex):
            if startindex == len(s):
                res.append(record[:])
                return

            for i in range(startindex, len(s)):
                tmp = s[startindex:i + 1]
                if tmp == tmp[::-1]:
                    record.append(tmp)
                    backtrack(s, i + 1)
                    record.pop()
                else:
                    continue

        backtrack(s, 0)

        return res
