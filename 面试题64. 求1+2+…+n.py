class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 核心思想：利用 and 逻辑判断的短路来实现递归的终止
        return n != 0 and n + self.sumNums(n - 1)

s = Solution()
print(s.sumNums(3))

