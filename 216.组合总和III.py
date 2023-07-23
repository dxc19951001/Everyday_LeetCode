from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        # 核心思想--回溯
        # 与39题类似的思路

        result = []
        def recall(last, start, tmp):
            
            # last：剩余的数
            # start：开始的数
            # tmp：记录已取的数

            for i in range(start, 10):
                if i == last and len(tmp) == k-1:
                    # 如果i等于剩下的数且当前tmp长度等于k-1
                    # 则此集合为答案
                    result.append(tmp+[i])
                elif i < last:
                    # 如果i小于剩下的数，则进入下层递归
                    recall(last-i, i+1, tmp+[i])
                
                elif i > last or len(tmp) > k:
                    # 如果i大于剩余的数 或者 tmp的长度大于k
                    # 则进行回溯
                    return
        recall(n, 1, [])
        
        return result
    
    def combinationSum3_1(self, k: int, n: int) -> List[List[int]]:

        # 核心思想--回溯
    
        res = []

        def helper(first=1, cur_sum=0, cur=[]):
            if len(cur) == k and cur_sum == n:
                # 如果cur长度为k，且 cur_sum的和为0
                # 则为1个解
                res.append(cur[:])
            
            for i in range(first, 10):
                # 进入递归
                helper(i+1, cur_sum+i, cur+[i])
            
        helper()

        return res

    def combinationSum4(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # 核心思想：回溯
        res = []
        sum_ = []
        # 1.确定参数：确定回溯参数：n，k, startindex(每次循环的起始位置）
        # 2.确定终止条件：
        #   len(sum_) == k and sum(sum_) == n，则找到可需要的解
        #   len(sum_) > k or sum(sum_) > n，则说明再往后找找不到了，进行剪枝
        # 3.单层循环：
        #   从1循环到10
        def backtrack(k, n, startindex):
            if len(sum_) == k and sum(sum_) == n:
                res.append(sum_[:])
                return

            if len(sum_) > k or sum(sum_) > n:
                return

            for i in range(startindex, 10):
                sum_.append(i)
                # 由于数字不重复，startindex每次递归需要+1
                backtrack(k, n, i + 1)
                sum_.pop()

        backtrack(k, n, 1)

        return res