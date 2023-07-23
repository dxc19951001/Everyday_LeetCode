# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 45.跳跃游戏 II.py
    @date：2023/1/10 14:16
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 核心：贪心算法
        # curdisantace表示当前覆盖的距离
        # maxdistance表示当前所能覆盖的最大距离
        # 遍历nums，当遍历到一个元素时，从当前元素触发所能到达的最大距离 与 之前元素的最大距离比较，取得maxdistance
        # 当遍历元素到curdisantace时，更新curdisantace到maxdistance，表示下一个能覆盖的距离增加了
        # 同时step 加1，表示继续向下走了一步，当curdisantace >= len(nums) - 1，表示走完了

        if len(nums) == 1:
            return 0

        step, curdisantace, maxdistance = 0, 0, 0

        for i in range(len(nums) - 1):
            maxdistance = max(maxdistance, nums[i] + i)
            if i == curdisantace:
                curdisantace = maxdistance
                step += 1
                if curdisantace >= len(nums) - 1:
                    return step