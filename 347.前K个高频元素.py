from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 核心思想--暴力求解
        # 字典的key为nums中的值，val为该值出现的次数
        # 对字典按照val的大小进行倒序排序
        # 取前k个元素输出即为答案
        
        dicts = dict()
        set_list = set(nums)

        for i in set_list:
            dicts[i] = nums.count(i)
        
        a = sorted(dicts.items(), key=lambda x: x[1], reverse=True)
        # items()方法将字典的元素转化为了元组，而这里key参数对应的lambda表达式的意思则是选取元组中的第二个元素作为比较参数

        ans = list()
        for j in range(k):
            ans.append(a[j][0])
     
        return ans
    

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:

        # 改进版本

        dict = {}
        res = []
        for i in nums:
            dict[i] = 1 if i not in dict else dict[i] + 1
        res = sorted(dict.items(), key = lambda x : x[1], reverse = True)
        a = []
        if len(res) >= k:
            for i in range(k):
                a.append(res[i][0]) 
            return a
        else:
            return []

    
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        # 利用Counter
        counter = Counter(nums)
        a = sorted(counter.items(),key = lambda a:a[1],reverse=True)
        res = []
        for i in range(k):
            res.append(a[i][0])
        return res