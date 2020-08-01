import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        # 核心思想--最小堆
        # 在堆heap中放入每个列表的第一个元素，堆中元素的最大值和最小值，即为区间范围res
        # 利用堆的性质，每次从堆中弹出最小的一个元素，
        # 并将该元素所在列表的下一个元素存入堆中，因为由题可知，列表都是有序的，往下一个元素移动，res范围可能会变小
        # 维护最大值与最小值，若区间范围变小，则更新res
        # 当弹出的数是对应序列的最后一个值的时候，跳出循环，返回最终的res


        heap = []  # 设定一个堆
        n = len(nums) 
        mi = float('inf')
        ma = float('-inf')
        for i in range(n):
            heapq.heappush(heap, (nums[i][0], 0, i))  # 将每个列表的第一个元素放入堆中
            # 堆中每一个元素包含该元素的：值、所在列表中的位置，所在列表
            mi = min(mi, nums[i][0])
            ma = max(ma, nums[i][0])

        res = [mi, ma]  # 取值范围
        while True:
            cur = heapq.heappop(heap)  # 弹出堆中最小的元素
            if cur[1] == len(nums[cur[2]]) - 1:
                # 当弹出的元素是所在列表中的最后一个元素时，则结束循环
                break
            heapq.heappush(heap, (nums[cur[2]][cur[1]+1], cur[1]+1, cur[2]))  # 将弹出元素所在列表的下一个元素加入
            ma = max(ma, nums[cur[2]][cur[1]+1])  # 更新此时堆中的最大值
            mi = heap[0][0]  # 更新测试堆中的最小值
            # 根据题目判断范围大小的两种情况，判断此时的res范围是否缩小，缩小则更新res
            if ma-mi < res[1]-res[0]:  
                res = [mi, ma]
            elif ma-mi == res[1]-res[0] and mi < res[0]:
                res = [mi, ma]
        return res
