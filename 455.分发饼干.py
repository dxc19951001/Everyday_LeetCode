# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 455.分发饼干.py
    @date：2023/1/9 15:04
"""


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 优先喂胃口小的
        if not g or not s:
            return 0
        g.sort()
        s.sort()

        count = 0
        for i in range(len(s)):
            if count < len(g) and s[i] >= g[count]:
                count += 1

        return count

