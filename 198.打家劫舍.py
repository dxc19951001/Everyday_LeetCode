from typing import List
import time

class Solution:

    def rob(self, nums: List[int]) -> int:

        # 非递归，动态规划
        # 核心思想：
        # 从屋子选、不选的角度出发，使用动态规划，依次向前推到
        # 边界条件为：没有房间时返回0；1间房间只能偷此房间；2间房间偷2间中最大的
        # 从而推导出有n间房时，能偷的最大金额

        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            A = dp[i - 2] + nums[i]  # 选
            B = dp[i - 1]  # 不选
            dp[i] = max(A, B)
        
        return dp[size - 1]
    
    
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


