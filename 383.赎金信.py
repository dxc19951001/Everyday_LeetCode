# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 383.赎金信.py
    @date：2023/1/2 21:44
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # 核心思想：hash表
        # 循环magazine，存储到字典中，key为字母，val字母出现的次数
        # 循环ransomNote，当字母在字典中时，且该字母的val不为0，字典中字母的val减一
        # 如果字典中有元素都没有找到则返回False
        # 都循环完返回True

        mag_dict = dict()

        for i in magazine:
            if i in mag_dict:
                mag_dict[i] += 1
            else:
                mag_dict[i] = 1

        for i in ransomNote:
            if i in mag_dict and mag_dict[i] != 0:
                mag_dict[i] -= 1
            else:
                return False
        return True