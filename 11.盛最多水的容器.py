# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 11.盛最多水的容器.py
    @date：2023/1/12 16:40
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 双指针
        # 指针更新条件：当左指针的高度小于右指针时，更新左指针，反之更新右指针

        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            tmp = (right - left) * min(height[right], height[left])
            res = max(res, tmp)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res
