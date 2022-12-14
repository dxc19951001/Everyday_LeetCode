from typing import List


class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:

        # 核心思想
        # 暴力循环，枚举法

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 核心思想
        # 用字典模拟哈希求解
        # 使用enumerate函数，获得每个数值对应下标index和数值nums
        # 并以nums为key，index为下标存入hashmap字典中
        # 每次循环计算another_num = target - num，若another_num在hashmap字典中
        # 则返回another_num的下标hashmap[another_num]和此时数值的下标index
        
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None

# 哈哈哈