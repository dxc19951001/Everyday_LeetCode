# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 49.字母异位词分组.py
    @date：2023/2/2 15:43
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # hash表，以排序后的字符串为key，如果key相同则加入到同一个列表中
        hash_dict = {}

        for i in strs:
            keys = "".join(sorted(i))
            if keys in hash_dict:
                hash_dict[keys].append(i)
            else:
                hash_dict[keys] = [i]
        return list(hash_dict.values())
