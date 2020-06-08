class Solution:
    def new21Game_0(self, N: int, K: int, W: int) -> float:

        # 核心思想：
        # 到手中点数在K到N之间，满足条件，即概率为1，即[K,N]的概率为1
        # 题意每次抽取都是独立的，其结果具有相同的概率，所以是有放回的抽取
        
        # 当手点数在K-1时，还需要从W中抽一张牌,计算抽取后手中的点数范围为[K，K-1+W]
        # 判断[K，K-1+W]有多少范围[K,N]中，就有几个1,再乘以每个抽到每个数字的概率1/W
        # 可以得出手中点数在K-1时，满足条件的概率
        
        # 当手中点数在K-2时，还需要从W中抽一张牌,计算抽取后手中的点数范围为[K-1，K-2+W]
        # 其中K-1满足概率已经算出，再加上[K-1，K-2+W],有多少范围[K,N]中，就有几个1
        # 再乘以每个抽到每个数字的概率1/W，
        # 可以得出手中点数在K-2时，满足条件的概率

        # 依次类推，得到手中点数为0时，即刚开始玩游戏时，满足条件的概率
        
        #创建一个全0数组，长度为K+W
        dp = [0.0]*(K+W)

        # 当手中点数为K到N之间时，满足条件，概率为1
        # for k in range(K,N+1):
        # 考虑到N>K+W时，超过了设置的全零数组长度，会报错
        # N-(K+W)的数据并不会造成影响
        # 所以取min(N+1, K+W)

        for k in range(K,min(N+1, K+W)):
            dp[k] = 1.0
        
        # 当手中点数为0到K-1时，计算每个点数满足条件的概率
        # 目标是手中点数为0即刚开始玩时，满足条件的概率
        for k in range(K-1, -1, -1):
            tem = 0
            for j in range(W):
                tem += dp[k+j+1]
            dp[k] = tem/float(W)
        
        return dp[0]
    
    
    def new21Game(self, N: int, K: int, W: int) -> float:
        
        #创建一个全0数组，长度为K+W
        dp = [0.0]*(K+W)

        # 当手中点数为K到N之间时，满足条件，概率为1
        # for k in range(K,N+1):
        
        # 考虑到N>K+W时，超过了设置的全零数组长度(K+W)，会报错
        # 因为N-(K+W)的数据并不会造成影响
        # 所以取min(N+1, K+W)

        for k in range(K, min(N+1, K+W)):
            dp[k] = 1.0
        
        # 当手中点数为0到K-1时，计算每个点数满足条件的概率
        # 目标是手中点数为0即刚开始玩时，满足条件的概率
        # S = N-K+1
        # N-K+1>W时，最多也只有W个数为1
        S = min(N-K+1, W)
        for k in range(K-1, -1, -1):
            dp[k] = S/float(W)
            S += dp[k]-dp[k+W]
        
        return dp[0]

s = Solution()
a = s.new21Game(28, 17, 10)
print(a)


