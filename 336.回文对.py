from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        # 核心思想--暴力解法
        # 最后运行时间超时了，看评论js和c可以通过暴力求解

        n = len(words)
        ans = list()
        for i in range(n):
            for j in range(n):
                if j != i:
                    tmp =  words[i] + words[j]
                    if tmp == tmp[::-1]:
                        ans.append([i, j])
        return ans

    def palindromePairs1(self, words: List[str]) -> List[List[int]]:

        # 核心思想--枚举前缀和后缀
        # 如果两个字符串k1，k2组成一个回文字符串会出现三种情况
        # len(k1) == len(k2),则需要比较k1 == k2[::-1]
        # len(k1) < len(k2),例如，k1=a, k2=abb,可组成abba
        #   因为k2后缀bb已经是回文字符串了，则需要找k1与k2剩下相等的部分
        # len(k1) > len(k2),例如，k1=bba, k2=a,组成abba
        #   因为k1前缀bb已经是回文字符串了，则需要找k1剩下与k2相等的部分

        res = []
        worddict = {word: i for i, word in enumerate(words)}  # 构建一个字典，key为word，valie为索引
        for i, word in enumerate(words):
            # i为word索引，word为字符串
            for j in range(len(word)+1): 
                # 这里+1是因为，列表切片是前闭后开区间
                tmp1 = word[:j]  # 字符串的前缀
                tmp2 = word[j:]  # 字符串的后缀
                if tmp1[::-1] in worddict and worddict[tmp1[::-1]] != i and tmp2 == tmp2[::-1]:
                    # 当word的前缀在字典中，且不是word自身，且word剩下部分是回文(空也是回文)
                    # 则说明存在能与word组成回文的字符串
                    res.append([i, worddict[tmp1[::-1]]])  # 返回此时的word下标和找到的字符串下标

                if j > 0 and tmp2[::-1] in worddict and worddict[tmp2[::-1]] != i and tmp1 == tmp1[::-1]:         
                    # 当word的后缀在字典中，且不是word自身，且word剩下部分是回文(空也是回文)
                    # 则说明存在能与word组成回文的字符串
                    # 注意：因为是后缀，所以至少要从word的第二位算起，所以j>0
                    res.append([worddict[tmp2[::-1]], i])  # 返回此时的word下标和找到的字符串下标
        return res