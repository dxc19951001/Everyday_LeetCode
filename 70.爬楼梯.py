class Solution(object):
    def climbStairs_rec(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 核心思路
        # 采用递归的方式
        # 每次爬1阶或者2阶台阶
        
        # 递归终止条件
        # 爬到最后还剩2阶或1阶台阶时，即n=1或2
        # 剩1阶只有1钟方法；剩2阶只有2钟方法（11或2）
        # 直接返回n就可以了

        # 例如n = 4
        # 4第一次爬2阶，剩2
            # 剩2，则有2种方法
        # 4第一次爬1阶，剩3
            # 第二次爬1，剩2，则有两种方法
            # 第二次爬2，剩1，则有一种方法
        # 则合计一共2+2+1=5种

        # 递归的重叠子问题多了，n大了超出运算时间

        if n > 2:
            ans = self.climbStairs_rec(n-1) + self.climbStairs_rec(n-2)
        else:
            ans = n  
        return ans
        
    from functools import lru_cache
    @lru_cache(100)
    def climbStairs_cacherec(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 核心思路
        # 给递归加上缓存器可成功应对大数据

        if n > 2:
            ans = self.climbStairs_cacherec(n-1) + self.climbStairs_cacherec(n-2)
        else:
            ans = n  
        return ans

    def climbStairs_dp(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 核心思路
        # 使用动态规划额方法
        # 爬到第n层的最后一步剩1阶或2阶
        # 则剩1阶方法数为：走前n-1阶台阶的方法数+1
        # 则剩2阶方法数为：走前n-2阶台阶的方法数+2
        # 由此可以推出总方法数：dp[i] = dp[i-1] +dp[i-2]
        # 边界值：dp[0]=1;dp[1]=2
        # 可以发现这题本质是个斐波那契数列

        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2          

        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

    def climbStairs_fibo(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 核心思想
        # 运用斐波那契数列递推公式求解
        # 由于dp[i]只和dp[i-1]和dp[i-2]有关
        # 也是运用了滚动数组的思想
        a = 1
        b = 1
        ans = 1
        for i in range(n-1):
            ans = a + b
            a, b = b, ans
        return ans

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 同样是滚动数组
        # 只用了两个常数变量效率最高
        ans = 1
        b = 1
        for i in range(n):
            ans = ans + b
            ans, b = b, ans
        return ans
    