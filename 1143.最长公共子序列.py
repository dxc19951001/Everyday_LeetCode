# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 1143.最长公共子序列.py
    @date：2022/12/31 1:28
"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # 参考：718.最长重复子数组
        # 二维的dp数组
        # 注意：当字符不相同的时候，状态由上边和右边，最大的转移得到

        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        res = 0
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                res = max(res, dp[i][j])
        # print(dp)
        return res