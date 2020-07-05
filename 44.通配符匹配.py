class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # 核心思想
        # 动态规划
        # 构建一个 len(s)+1 * len(p)+1 的dp动态矩阵
        # 加1是因为：考虑s或p为空的情况下的初始状态
        # 1.s和p都为空时，dp[0][0] = True
        # 2.当p第一个字符为'*'，则dp第一行全部可以匹配，即dp[1] = [True]*i
        # 3.当p的前几个字符为'*',则dp第一列从1开始的前几个状态都为True，因为*可以表示空
        # 根据1、2、3，dp矩阵的初始状态设置完毕
        # 例如s='a',p='**a'，
        # dp=[[F,F],[F,F],[F,F],[F,F]]--根据1-->[[T,F],[F,F],[F,F],[F,F]]
        # --根据2-->[[T,F],[T,T],[F,F],[F,F]]--根据3-->[[T,F],[T,T],[T,F],[F,F]]
        
        # for m in range(1, i):
        #   for n in range(1, j):
        # 开始遍历dp数组，注意m和n是dp数组上的索引，不是s和p的索引
        # 因为i = len(s)+1；j = len(p)+1，所以m和n要变成s和p的索引需要减1
        # 其中m代表列，n代表行
        # 4.若s[m-1] == p[n-1] or p[n-1] == '?'，说明此dp位置上s和p的值相等，
        # 则此位置上的值等于左斜上方的值，dp[n][m] = dp[n-1][m-1]
        # 5.若p[n-1] == '*'，并且此位置的正上方位置dp[n-1][m]==True
        # 则此列从p[n-1]位置开始到这行的最后都可以匹配，因为'*'可以为空，也可以为任意字符串
        # 最终返回dp[-1][-1]即为结果

        # 例如s='a',p='**a'
        # dp初始化后=[[T,F],[T,T],[T,F],[F,F]]--根据4-->[[T,F],[T,T],[T,T],[F,F]]
        # --根据5-->[[T,F],[T,T],[T,F],[F,T]]

        # 参考图解:https://leetcode-cn.com/problems/wildcard-matching/solution/yi-ge-qi-pan-kan-dong-dong-tai-gui-hua-dpsi-lu-by-/
        
        # i代表列，j代表行
        i = len(s)+1
        j = len(p)+1
        dp = [[False]*i for _ in range(j)]
        dp[0][0] = True

        
        if p.startswith('*'):
            # p以'*'开头，则第一行全部可以匹配
            dp[1] = [True]*i
        
        for k in range(len(p)):
            # p开头有几个'*',则第一列从1开始的前几个状态都为True
            if p[k] == '*':
                dp[k+1][0] = True
            else:
                break
        
        for m in range(1, i):
            for n in range(1, j):
                # m代表列，n代表行
                
                if s[m-1] == p[n-1] or p[n-1] == '?':
                    dp[n][m] = dp[n-1][m-1]

                if p[n-1] == '*' and dp[n-1][m]:
                    dp[n][m:] = [True]*(len(s[m:])+1)

        return dp[-1][-1]
        
        
        

x = Solution()
s = "ho"
p = "**ho"
print(x.isMatch(s, p))