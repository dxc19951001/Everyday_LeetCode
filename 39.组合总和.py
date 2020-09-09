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
        
        candidates = sorted(candidates)       
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
                    # 如果当前元素 大于 last
                    # 说明此次递归已结束，进行回溯，返回到上一层递归中
                    # 上一层递归中的for循环i进入下一个数 
                    return
        combination(0, [], target)
        
        return res

s = Solution()

candidates = [2,3,6,7]
target = 7

a= s.combinationSum(candidates, target)

print(a)