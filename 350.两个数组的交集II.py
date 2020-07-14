from typing import List
import collections

class Solution:
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # 核心思想
        # 巧妙解法
        # 对nums1和nums2运用set去重后，使用&得到两个列表中相同的数的机会inter
        # 循环inter，每次判断其中的元素i在nums1和nums2出现的次数
        # 并乘以其中最小的次数，即为该元素在集合中出现的次数

        inter = set(nums1) & set(nums2)
        print(inter)
        l = []
        for i in inter:
            l += [i] * min(nums1.count(i), nums2.count(i))  
        return l
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # 核心思想
        # 运用hash表
        # 将nums1和nums2中长度较短的，变成hash表
        # 其中key为其中元素，value为这个元素出现了几次
        # 例如[1, 2, 3, 1]变为hash表为：{1:2, 2:1, 3:1}
        # 这里可运用collections.Counter()模块，很轻松发的做到

        # 循环遍历nums1和nums2中长度较长的
        # 如果循环到的元素在hash表中
        #  1.将其添加到intersection列表中，2.将hash表中该元素的value值减1，减至0时，直接删除该元素
        # 最终返回intersection

        if len(nums1) > len(nums2):
            # 比较长度
            # 将较短的列表变成hash表
            return self.intersect(nums2, nums1)
        
        m = collections.Counter()
        for num in nums1:
            m[num] += 1
        
        intersection = list()
        for num in nums2:
            if m.get(num, 0) > 0:
                # m.get(num, 0)若遍历到元素在hash表中，返回value值，
                # 若遍历到的元素不在hash表中，则返回默认值0
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)
        
        return intersection

