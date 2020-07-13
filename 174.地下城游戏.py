from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        # 核心思想
        # 因为要最低初始健康点数，所从后向前，反向dp求解，返回dp[0][0]即为答案
        
        # dp[i][j]是进入每一个房间时的初始健康点数
        # 则进入下一个房间的健康点数为，dp[i][j]+此时房间的健康点数。下一个房间为下房间或右房间
        # dp[i+1][j] = dp[i][j] + dungeon[i][j] 或 dp[i][j+1] = dp[i][j] + dungeon[i][j]
        # 所以动态转移方程为：dp[i][j]=dp[i+1][j] - dungeon[i][j] 或 dp[i][j]=dp[i][j+1] - dungeon[i][j]
        # 由于求最小的初始健康点数，因此从该房间进入下一个房间时，dp[i][j]应该为最小值
        # 由上述两个动态转移方程可知，要使得dp[i][j]最小，则应该往下一个初始健康点数dp小的房间走
        # 即min(dp[i+1][j], dp[i][j+1])，下方房间和右边房间哪个dp值小，就往哪个房间走
        # 所以动态转移方程为：dp[i][j]= min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
        
        # 此时动态转移方程可能会出现负值，是因为[i][j]房间为恢复能量，即dungeon[i][j]为一个较大正值
        # 在此房间给勇者恢复血量后，勇者的血量大大超过了前往下一个房间所需的最低初始健康值，
        # 则此时，勇者进入[i][j]房间的健康值应该为最低的1，即dp[i][j] = 1
        # 所以最终动态转移方程为：dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
        
        # n, m = len(dungeon), len(dungeon[0])
        # 设置一个n*m的dp数组,其中的值都是较大值，

        # 设定初始值
        # 其中最后一个房间为dp[n-1][m-1],经历过战斗后，勇士最终健康值剩1
        # 设最后一个房间的下房间和左房间的值都为1：dp[n][m - 1] = dp[n - 1][m] = 1
        # 即救出公主，走出地下城的最小健康值最为1

        n, m = len(dungeon), len(dungeon[0])  # n是行，m是列
        BIG = 10**9
        dp = [[BIG] * (m + 1) for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)

        return dp[0][0]