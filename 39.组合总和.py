from typing import List

class Solution:
    def combinationSum(self, candidates, target):
        # 核心思想--回溯

        ans = []
        temp = []
        def recursion(idx, res):
            # idx当前数的索引
            # res为当前索引的累加和 
            if idx >= len(candidates) or res > target:
                # 当索引超过的数组的长度 或者 累加和超过的target
                # 显然是不合适的，进行回溯
                return
            if res == target:
                # 当累加和正好等于target
                # 添加到ans中，并进行回溯
                ans.append(temp[:])
                return

            temp.append(candidates[idx])  # temp中记录已经寻找过的元素
            recursion(idx, res + candidates[idx])   # 进行回溯
            temp.pop()  # 跳出上层回溯后，去除末尾元素
            recursion(idx + 1, res)  # 进入下一层回溯
        recursion(0, 0)
        return ans 


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # 核心思想--回溯+剪枝
        
        candidates = sorted(candidates)  # 对candidates进行排序      
        n = len(candidates)
        res =[]
        
        def combination(s, old, last):
            # s：当前开始索引位置
            # old：已记录元素的列表
            # last：距离target还是差多少
            for i in range(s, n):
                # 从s到n开始循环
                if candidates[i] == last:
                    # 如果当前元素 等于 last
                    # 将已记录元素加上当前元素，为一个解
                    res.append(old+[candidates[i]])  
                if candidates[i] < last:
                    # 如果当前元素 小于 last
                    # 进入下一次递归
                    # 从当前元素开始，old加上此元素，last减去当前元素
                    combination(i, old+[candidates[i]], last-candidates[i])  
                if candidates[i] > last:
                    # 如果当前元素 大于 last，由于已经对candidates进行排序了，后面的元素只会比当前元素更大
                    # 所以此次递归已结束，进行回溯，返回到上一层递归中
                    # 上一层递归中的for循环i进入下一个数 
                    return
        combination(0, [], target)
        
        return res

    def combinationSum3(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 1.确定参数：确定回溯参数：candidates，target, startindex(每次循环的起始位置）
        # 2.确定终止条件：
        #   len(sum_) == k and sum(sum_) == n，则找到可需要的解
        #   len(sum_) > k or sum(sum_) > n，则说明再往后找找不到了，进行剪枝
        # 3.单层循环：
        #   从1循环到10
        res = []
        sum_ = []

        def backtrack(candidates, target, startindex):
            if sum(sum_) == target:
                res.append(sum_[:])
                return
            if sum(sum_) > target:
                return

            for i in range(startindex, len(candidates)):
                sum_.append(candidates[i])
                # 由于数字可以重复，startindex每次递归就位i
                backtrack(candidates, target, i)
                sum_.pop()

        backtrack(candidates, target, 0)
        return res

s = Solution()

candidates = [2,3,6,7]
target = 7

a= s.combinationSum(candidates, target)

print(a)
