from typing import List

class Solution:
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:

        # 核心思想（此题与No.1题目类似)
        # # 用字典模拟哈希求解
        # 使用enumerate函数，获得每个数值对应下标index和数值num
        # 并以num为key，index为下标存入hashmap字典中
        # 每次循环numbers时，计算another_num = target - num，若another_num在hashmap字典中
        # 则返回another_num的下标hashmap[another_num]，和此时数值num的下标index
        # 由于返回的下标值（index1 和 index2）不是从零开始的，所以得出的答案需要 +1
        # 并且要求其中 index1 必须小于 index2，所以使用sorted函数对结果排序

        hashmap = {}
        for index, num in enumerate(numbers):
            another_num = target - num
            if another_num in hashmap:
                return sorted([hashmap[another_num]+1, index+1])
            hashmap[num] = index
        return None

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # 核心思想
        # 双指针，注意此题是有序序列，所以可以用双指针解法，这是与第一题不同的地方
        # low指针指向头，high指针指向尾
        # total = numbers[low] + numbers[high]
        # 如果total == target，返回[low + 1, high + 1]
        # 如果total < target，low指针向右移一位
        # 如果total > target，high指针向左移一位
        # 若low指针>=high指针位置时，则循环结束。

        low, high = 0, len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1, high + 1]
            elif total < target:
                low += 1
            else:
                high -= 1

        return [-1, -1]

