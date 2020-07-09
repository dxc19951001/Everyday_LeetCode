from typing import List

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        
        # 核心思想
        # 动态规划
        # dp[i] 表示字符串的前 i 个字符的最少未匹配数。（i为字符串下标）
        # 假设当前我们已经考虑完了前 i -1个字符了，对于前 i 个字符对应的最少未匹配数：
        # 1.第 i 个字符未匹配，则 dp[i] = dp[i-1] + 1，即不匹配数加 1;
        # 2.遍历前 i-1 个字符，若其中某一个字符的下标 idx 为开头、以第 i 个字符为结尾的字符串,正好是词典里的某个单词dic，
        #   则idx = i + 1 - len(dic)，（i+1代表第i位的字符串个数）
        #   说明sentence[i + 1 - len(dic):i+1]字符串在字典中有为匹配的字符串，(注意列表左闭右开，所以取i+1)
        #   且到dp[i]为止没有匹配的只是dp[idx-1]，即dp[i - len(dic)]之前没有匹配的
        #   但是如果选择了该字符串，反而使得未匹配字符变多了，则不应该匹配该字符串
        #   所以dp[i] = min(dp[i-1], dp[i - len(dic)]) 更新 dp[i]。
        # 注意这里设置动态列表时要设置n+1个0的列表，因为在python中dp[-1]将取到最后一个值
        # 当dp[0] = dp[0 - 1] + 1 = dp[-1]+1 = 1
        # 最终返回dp[-2]即为答案，（dp[-1]只是用来计算用的）

        # 特殊情况
        # sentence为空返回0
        # dictionary为空，返回len(sentence)

        # 例如 dictionary = ["Leet","etc","code","Go"]
        # sentence = "LeetcodeGood"
        # 0位是L不匹配字典,dp[0]=dp[0 - 1] + 1 = dp[-1]+1 = 1
        # 1位是e不匹配字典，dp[1]=dp[1-1]+1 = dp[0]+1 = 2
        # 2位是e不匹配字典，dp[2]=dp[2-1]+1 = dp[1]+1 =3
        # 3位是t和前面的字符可组合为Leet匹配字典，dp[3]=dp[3-1]+1 = dp[2]+1 = 4
        #   sentence[i + 1 - len(Leet):i+1] = sentence[0:4] = Leet
        #   dp[i - len(Leet) = dp[3-4] = dp[-1] = 0 
        #   dp[3] = min(dp[3],dp[-1]) = 0
        # 4位是c匹配字典，dp[4]=dp[4-1]+1 = dp[3]+1 = 1
        #   注意此时，c和前面的字符可组合成etc在字典中
        #   sentence[i + 1 - len(etc):i+1] = sentence[2:5] = etc
        #   dp[i - len(etc) = dp[4-3] = dp[1] = 2
        #   矛盾出现了，如果匹配字符，反而使得未匹配字符数变多，所以不进行匹配
        #   所以dp[4] = min(dp[4],dp[1]) = 1
        #  后续类似往下推导
        # 最终dp=[1, 2, 3, 0, 1, 2, 3, 0, 1, 0, 1, 2, 0]
        # 返回dp[-2] = 2 即为答案

        
        if len(sentence) <= 0: return 0
        if len(dictionary) <= 0: return len(sentence)

        dp = [0] * (len(sentence) + 1)  # 最后一个0是计算用的
        for i in range(len(sentence)):
            dp[i] = dp[i - 1] + 1
            # 遍历所有单词，看能否和「以i为结尾的子串」一样
            for dic in dictionary:
                if (len(dic) <= i + 1) and sentence[i + 1 - len(dic):i + 1] == dic:
                    # 只有从sentence取出字符串长度，大于等于字典中单词的长度时，才可以取出此单词
                    # 否则i + 1 - len(dic) 会取得负数，这样相当于取到sentence后面的数，不符合逻辑
                    dp[i] = min(dp[i], dp[i - len(dic)])
        return dp[-2]
