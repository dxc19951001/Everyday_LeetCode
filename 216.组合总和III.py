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