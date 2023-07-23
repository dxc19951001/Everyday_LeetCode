# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 278.第一个错误的版本.py
    @date：2023/1/14 0:46
"""


def isBadVersion(version):
    pass


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 二分查找
        # isBadVersion返回False表示没出错，mid之前的都没错，则再[mid+1,right]中继续找
        # isBadVersion返回True表示出错了，mid之后的都是错的，则再[left,mid-1]中继续找
        # 直到left>right，返回left
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            print(isBadVersion(mid))
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left