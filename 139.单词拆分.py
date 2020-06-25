class Solution(object):
    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 核心思想：
        # 设置一个列表breakp用来存储
        # 所有能够组成wordDict中字符串的节点
        # 注意：字符串、列表的切片时前闭后开的，后面的节点时取不到的
        # 若最终存储的最后一个节点不是字符串的长度，则返回false
        # 若是字符串的长度则返回True

        breakp = [0]

        for i in range(len(s) + 1):
            for j in breakp:
                if s[j:i] in wordDict:
                    breakp.append(i)
                    break
        return breakp[-1] == len(s)

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        # 核心思想动态规划
        # 初始化dp=[False,⋯,False]，
        # 长度为n+1。n为字符串长度。dp[i]表示s的前i位是否可以用wordDict中的单词表示。

        # 初始化dp[0]=Truedp[0]=True，空字符可以被表示。
        # 遍历字符串的所有子串，遍历开始索引i，遍历区间[0,n)：
        # 遍历结束索引j，遍历区间[i+1,n+1)：

        # 若dp[i]=True且s[i,⋯,j)在wordlist中：dp[j]=Truedp[j]=True。
        # 解释：dp[i]=True说明s的前i位s[:i]存在可以用wordDict表示，
        # 则s[i,⋯,j)出现在wordDict中，说明s[i,j]可以用wordDict表示。
        # 最终判断dp中最后是否为True

        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    print(s[i:j])
                    print(i, j)
                    dp[j] = True
        print(dp)
        return dp[-1]
