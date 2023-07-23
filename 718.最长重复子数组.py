from typing import List


class Solution:
    def findLength1(self, A: List[int], B: List[int]) -> int:
        # 核心思想
        # 暴力枚举求解
        # 从A中的每一个元素开始向后循环，在列表A循环的中，B列表每次从第一个数字开始循环
        # 设每次最长公共前缀为k，若A[i+k] == B[j+k]，则k += 1
        # 记录每个A中每个元素为开头的序列，与B中每个元素为开头的序列的，长度最长的子数组的长度。
        # 若比上一次k大则更新k
        # 时间复杂度为O(n^3),虽然简单但长的列表，超出时间限制

        ans = 0
        for i in range(len(A)):
            for j in range(len(B)):
                k = 0
                while A[i+k] == B[j+k]:
                    k += 1
                    if i+k > len(A)-1 or j+k > len(B)-1:
                        break
                ans = max(ans, k)
        return ans

    def findLength(self, A: List[int], B: List[int]) -> int:
        
        # 核心思想
        # 动态规划
        # n为列表A长度+1，m为列表B长度+1
        # 加1是为了增加在A、B为空的情况
        # 生成一个n*m的全0二维列表dp
        # dp[i][j]表示列表A中的第i个，列表b中的第j个
        # 初始状态，当A或B为空时，dp[0][j]和dp[i][0]都为0
        # 若A[i-1]==B[j-1]，则dp[i][j] = dp[i-1][j-1]+1 否则 为0
        # 当前点的大小取决于当前点斜上方点的数值+1
        # 可参照图解：
        # https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/yi-zhang-biao-ba-ju-hua-kan-dong-dong-tai-gui-hua-/
        # 最终返回dp中最大的值

        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0  # 设置初始状态
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j-1]+1 if A[i-1] == B[j-1] else 0
                # 若 A[i-1] == B[j-1]，dp[i][j]的值取决于斜上方dp[i-1][j-1]的值加1
                # 为什么判断A[i-1] == B[j-1]，因为A列表和B列表的下标范围是[0,n-1]和[0，m-1]
                # 循环数字为[1,n]和[1,m],所以需要减1，不然会报错。
                ans = max(ans, dp[i][j])  # 本次循环中有比ans大的，更新ans
        return ans

    def findLength2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # 精简版
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        res = 0

        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])

        return res
