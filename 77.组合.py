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

    def combine1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 核心思想：回溯
        res = []
        path = []

        # 1.确定回溯参数：n，k, startindex(每次循环的起始位置）
        # 2.终止条件：当len(path) == k
        # 3.回溯搜索遍历：
        #   从startindex开始循环到n，左闭右闭区间
        #   每次节点加入到path中
        #   递归循环，每次startindex向后移一位
        #   到i循环完成后回溯，去掉当前的i进入到i+1
        def backtrack(n, k, startindex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startindex, n + 1):
                path.append(i)
                backtrack(n, k, i + 1)
                path.pop()

        backtrack(n, k, 1)

        return res


    def combin3(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 核心思想：回溯
        res = []
        path = []

        def backtrack(n, k, startindex):
            if len(path) == k:
                res.append(path[:])
                return
            # i表示从第几个元素开始循环
            # n - i表示剩余元素
            # k - len(path)表示要满足k个元素还需要的元素
            # 因此要满足：n-i >= k - len(path)
            # i <= n - (k - len(path))
            # 因为包括起始位置，我们要是一个左闭的集合
            # 因此在集合n中至多要从该起始位置 : i <= n - (k - path.size()) + 1，开始遍历
            # 由于python for循环左闭右开，所以要+2
            for i in range(startindex, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(n, k, i + 1)
                path.pop()

        backtrack(n, k, 1)

        return res
