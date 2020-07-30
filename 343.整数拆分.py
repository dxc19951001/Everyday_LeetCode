class Solution:
    def integerBreak1(self, n: int) -> int:

        # 核心思想--动态规划
        # dp[i]表示将正整数 i 拆分成至少两个正整数的和之后，这些正整数的最大乘积
        # 由于0不是正整数，1是最小的正整数，所有0和1都不能拆分，所有dp[0]=dp[1]=0
        # 当i >= 2 时，假设i拆分出的第一个正整数位j，j的取值范围时 1 到 i-1
        #   将i拆分成 j 和 i-j，且i-j不继续拆分，则此时乘积为 j*(i-j)
        #   将i拆分成 j 和 i-j，且i-j继续拆分，则此时乘积为 j*dp[i-j]
        # 所以当j固定，dp[i]=max(j*(i−j), j×dp[i−j])
        # 由于 j 的取值范围是 1 到 i-1，需要遍历所有的 j 得到 dp[i] 的最大值，
        # 若dp[i]比之前的大，则更新dp[i]
        # 因此可以得到状态转移方程如下：
        # dp[i]=max(dp[i], j *(i−j), j*dp[i−j])

        dp = [0] * (n + 1) # 设定一个n+1长度的dp列表
        for i in range(2, n + 1):
            # 遍历从2到n的数
            for j in range(1, i):
                # 将i拆分为 j 和 i-j，j的取值范围时1到i-1
                # 每次比较dp[i], j * (i - j), j * dp[i - j]，取最大值
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]

    def integerBreak(self, n: int) -> int:

        # 核心思想--数学解法
        # 结论：当正整数n拆分为至多个3相乘在乘以剩下的余数时，乘积最大

        if n <= 3:
            # 当n小于等于3时
            return n - 1
        
        quotient, remainder = n // 3, n % 3
        # n能分成多少个3，和除以3的余数
        if remainder == 0:
            # 余数为0，则为3的quotient次方
            return 3 ** quotient
        elif remainder == 1:
            # 余数为1，则为3的（quotient-1）次方乘4
            return 3 ** (quotient - 1) * 4
        else:
            # 余数为2，则为3的次方乘2
            return 3 ** quotient * 2
