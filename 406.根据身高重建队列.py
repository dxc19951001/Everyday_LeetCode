# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 406.根据身高重建队列.py
    @date：2023/1/10 16:44
"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 贪心算法，先确定一个维度，再确定另外一个维度
        # 维度一：按照身高降序排列，如果身高相同，则按照位置升序
        # 维度二：按照位置排序，进行排序
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []

        for i in people:
            queue.insert(i[1], i)

        return queue