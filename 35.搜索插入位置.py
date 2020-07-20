from typing import List


class Solution:
    def searchInsert1(self, nums: List[int], target: int) -> int:

        # 核心思想
        # 如果target在nums中，直接返回下标
        # 如果不在nums中
        #   如果在是插入nums中间，则返回第一个比target大的数的下标
        #   如果是插入末尾，则直接返回列表长度，因为将target插入nums后多一个数，target为最后一个数

        if target in nums:
            return nums.index(target)
        else:
            for i in nums:
                if target < i:
                    return nums.index(i)
            return len(nums)

    def searchInsert(self, nums: List[int], target: int) -> int:

        # 核心思想
        # 二分查找
        # 设置起始范围left, right = 0, len(nums)
        # 设置len(nums)原因是：nums可能会插入到末尾
        # 每次判断中间的数mid与targe的关系
        # 若中间的数小于target，则将left设置为mid+1
        # 若中间的数大于target，则将right设置为mid
        # 最终返回left即为插入的下标

        left, right = 0, len(nums)
        while left < right:
            mid = left+(right-left)//2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid
        return left
