class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        # 核心思想：
        # 原始公式为：A[i] + A[j] + i - j
        # 稍微给这个公式变形成：A[i] + i + A[j] - j，
        # 这样就可以看成是左A[i]+i和右A[j]-j两部分和的最大值。
        # 记录其结果res
        # 随着遍历数组，我们对两部分和取最大值，
        # 左A[i]+i和右A[j]-j两部分和res大于之前的res，则更新res
        # 并且若当前的值—下标对之和比之前更大，我们就更新left部分的值即可。
        
        # 首先left = A[0] + 0 =A[0]
        left, res = A[0], 0
        for j in range(1, len(A)):
            # 遍历数组，找出最大左A[i]+i和右A[j]-j
            res = max(res, left + A[j] - j)  # 判断res是否大于之前的值，若大于则更新
            left = max(left, A[j] + j)  # 判断下组值是否大于之前的值，大于则更新
        return res

s =Solution()
A = [8,1,5,2,6,3]
print(s.maxScoreSightseeingPair(A))