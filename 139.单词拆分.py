class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 核心思想：背包问题
        # dp[j]：长度为j的字符串，是否可以被拆分为一个或多个在字典中出现的单词，为布尔值
        # 动态转移方程：
        # 如果第i个单词不选，则dp[j] = dp[j]
        # 如果选择第i个单词，
        #   则长度为j的字符串已经用了j - len(wordDict[i]，根据dp定义判断dp[j - len(wordDict[i]]是True还是False
        #   在判读，j剩余的字符串为从j - len(wordDict[i])到j，是否与第i个单词相等，wordDict[i] == s[j - len(wordDict[i]):j]
        #   两个条件都满足的话，则第i个单词符合要求，返回True
        # 初始值：
        #   dp[0]就是递归的根基，dp[0]一定要为true

        dp = [False] * (len(s) + 1)
        dp[0] = True
        # 遍历背包
        for j in range(1, len(s) + 1):
            # 遍历单词
            for i in range(len(wordDict)):
                if j >= len(wordDict[i]):
                    dp[j] = dp[j] or (dp[j - len(wordDict[i])] and wordDict[i] == s[j - len(wordDict[i]):j])

        return dp[-1]

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

    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        # 核心思想动态规划
        # 初始化dp=[False,⋯,False]，
        # 长度为n+1。n为字符串长度。dp[i]表示s的前i位是否可以用wordDict中的单词表示。
        # 加1是为了初始dp[0]，表示没有字符串时，令dp[0]=True

        # 因为s要被空格拆分为一个或多个在字典中出现的单词，
        # 首先要满足s[:i]中有符合要求的单词
        # 所以dp[i] = True,i节点是可以拆开字符串s的节点，s[:i]为符合要求的单词
        # 若从i节点往后到j节点，s[i:j]也存在符合要求的单词，则dp[j] = True
        # 因此判断dp列表中为True的节点，需要dp[i] = True 和 (s[i:j] in wordDict)

        # 最终判断最后一个节点dp[-1]是否为True

        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            # 循环遍历字符串长度，找到分割点i
            for j in range(i+1, n+1):
                # 循环遍历，找到s[i:j]中符合要求的字符串，

                # i+1：表示从i节点的下一位开始找
                # n+1：由于range左闭右开，n+1只能取到n
                # 而字符串的切片也是左闭右开，n只能取到n+1，正好取到字符串最后一位

                if(dp[i] and (s[i:j] in wordDict)):
                    # 若i节点为true，可以以i节点分开，且s[i:j]在字符串中
                    # 则j节点也为true
                    dp[j] = True

        return dp[-1]


