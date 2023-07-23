# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 1046.最后一块石头的重量.py
    @date：2022/12/25 17:54
"""


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # 每次剔除列表中最大的两个元素，进行相减，如果不为0则添加到列表中
        # 但stones中的元素个数小于等于1个，说明都比较完了

        if not stones:
            return 0

        while len(stones) > 1:
            max_1 = stones.pop(stones.index(max(stones)))
            max_2 = stones.pop(stones.index(max(stones)))

            if max_1 - max_2:
                stones.append(max_1 - max_2)

        return stones[0] if stones else 0
