from typing import List
import time

class Solution:

    def rob(self, nums: List[int]) -> int:

        # 核心思想：动态规划
        # dp[i]含义:偷第i间房子时所能得到的最大金额
        # 动态转移方程：
        #   不偷第i间房，则最大金额为偷上一间房的最大金额，即dp[i-1]
        #   偷第i间房，则最大金额为偷上两间房的最大金额加上第i间房的金额，即 dp[i - 2] + nums[i]
        #   取最大值 max(dp[i - 1], dp[i - 2] + nums[i])
        # 初始状态：
        #   初始都为0

        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
    
    
    def rec_rob(self, nums, i) -> int:
        # 递归方法,会出现重叠子问题
        
        if i == 0:
            return nums[0]
        
        elif i == 1:
            return max(nums[0], nums[1])

        else:
            A = self.rec_rob(nums, i-2 ) + nums[i]  # 选第i个
            B = self.rec_rob(nums, i-1)  # 不选第i个
            return max(A, B)


nums = [1, 2, 4, 1, 7, 8, 3]

s = Solution()

print(s.rec_rob(nums, (len(nums)-1)))


print(s.rob(nums))


