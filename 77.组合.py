from typing import List
import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 核心思想--运用itertools函数
        return list(itertools.combinations(range(1,n+1),k))
    
    
    def combine2(self, n: int, k: int) -> List[List[int]]:

        # 核心思想--回溯剪支
        # 依次选择某个数字为开头，选择完长度为k的所有情况后，回溯

        result = []
        
        def recall(n, k, start, result, subset):
            # n为结束数字
            # k为选取长度
            # start为开始数字
            # result为最终结果
            # subset为每次需要填的数
            if len(subset) == k:
                result.append(subset[:])
                return
            for i in range(start, n+1):
                # 每次从[start, n]中选取一个数
                if k-len(subset) > n-i+1:
                    # 如果剩余要填的数（k - len(subset）大于 还能填的数的总和( n-i+1) 时，
                    # 往后永远无法完成题目要求的k个数的组合，这时可以剪枝
                    break
                subset.append(i)
                recall(n, k, i+1, result, subset)  # 进入递归，此时start变为i+1
                subset.pop()  # 结束上一层递归后，删除上一层放入subset的数字
        
        recall(n, k, 1, result, [])
        
        return result



