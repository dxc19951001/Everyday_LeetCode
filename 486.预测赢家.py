from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        # 核心思想--动态规划
        # 定义二维数组dp，其行数和列数都等于数组的长度
        # dp[i][j] 表示：当数组剩下的部分为下标 i 到下标 j 时，当前玩家与另一个玩家的分数之差的最大值
        #   注意：当前玩家是指当前选择数字的玩家，不一定是先手玩家
        # 由dp的定义可知，只有当 i <= j，数组剩下的部分才有意义，因此当 i>j 时，dp[i][j]=0
        
        # 实现对dp的初始化
        # 当 i=j 时，只剩一个数字，当前玩家只能拿取这个数字，因此对于所有 0 <= i < nums.length，都有dp[i][i]=nums[i]
        
        # 用 1 表示当前玩家，2 表示另一个玩家（1,2只是用来方便表述）
        # 当 i < j 时，当前玩家1可以选择 nums[i] 或 nums[j]，然后玩家2在数组剩下的部分选取数字。
        
        # 玩家1选择nums[i]，则玩家2在[i+1, j]中选取数字
        #   由dp的定义可知：dp[i+1,j]表示下标 i+1 到下标 j ，玩家2与玩家1分数之差的最大值
        #   此时玩家1比玩家2最多能获得的分数就是：nums[i] - dp[i + 1][j]
        
        # 玩家1选择nums[j]，则玩家2在[i, j-1]中选取数字
        #   由dp的定义可知：dp[i,j-1]表示下标 i 到下标 j-1 ，玩家2与玩家1分数之差的最大值
        #   此时玩家1比玩家2最多能获得的分数就是：nums[j] - dp[i][j - 1]

        # 在两种方案中，当前玩家会选择最优的方案，使得自己的分数最大化,会选择两种方案中差值较大的
        # 因此可以得到如下状态转移方程：
        # dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        # 因为dp[0][len(nums)-1]表示：数组下标 0 到下标 len(nums)-1 时，当前玩家与另一个玩家的分数之差的最大值
        # 即玩家1先选，与玩家2的差值   
        # 判断dp[0][len(nums)-1]，如果大于或等于 0，则先手得分大于或等于后手得分，因此先手成为赢家，否则后手成为赢家。

        # 优化点
        # 当len(nums)为偶数或n为1时，直接返回true
        # 对于偶数个数字的数组，玩家1一定获胜。
        #   因为如果玩家1选择拿法A，玩家2选择拿法B，玩家1输了。
        #   则玩家1换一种拿法选择拿法B，因为玩家1是先手，所以玩家1一定可以获胜。
        # 对于长度为1的数组，玩家1先拿，玩家2没有可拿的了，也必然获胜

        # 参考：https://leetcode-cn.com/problems/predict-the-winner/solution/yu-ce-ying-jia-by-leetcode-solution/

        n = len(nums)
        if n % 2 == 0 or n == 1:
            return True

        dp = [[0] * n for _ in range(n)]
        
        # 初始化dp
        for i, num in enumerate(nums):
            dp[i][i] = num
        
        for i in range(n - 2, -1, -1):
            # n-2表示从倒数第二列开始循环
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0

