# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 448.找到所有数组中消失的数字.py
    @date：2023/1/7 0:13
"""


class Solution(object):
    def findDisappearedNumbers1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 使用一个set集合去重，再用for循环记录从1-n,哪个数字不在set中
        set_num = set(nums)
        res = []

        for i in range(1, len(nums) + 1):
            if i not in set_num:
                res.append(i)

        return res

    class Solution(object):
        def findDisappearedNumbers2(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            # 原地记录
            # nums长度为n，应该记录数为[1,n]
            # 但是nums中有的数没出现，有的数出现了一次或者两次，要找的元素就是没有出现的元素
            # 因为如果是[1,n]每个元素都出现一次的话，nums中每个元素都可以看作是索引
            # 比如[1,3,2]对应的索引为[0,2,1]，nums中的数字对应一个索引位置，即nums中的数字和索引位置一一对应
            # 循环nums，将每个数字对应为索引的位置为：nums[i]- 1
            # 将nums[nums[i]) - 1]对应的数字变成负数，表示有数字和该位置对应
            # 若nums中剩下的有正数，说明正数所在的位置，没有数字和该位置对应，这就是没有出现的数字！
            # 注意：
            #   因为引入了负数，所以要用abs(nums[i])
            #   如果当前数字对应的索引位置已经是负数了，则表面该数字是重复数字，所以要跳过该数字
            for i in range(len(nums)):
                if nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] *= -1

            # print(nums)
            res = [i + 1 for i in range(len(nums)) if nums[i] > 0]
            return res