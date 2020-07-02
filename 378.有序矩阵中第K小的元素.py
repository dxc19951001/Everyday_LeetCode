from typing import List
import heapq


class Solution:
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:

        # 核心思想
        # 循环出矩阵中的每个元素
        # 运用sort进行排序
        # 返回第k个元素

        ans = list()
        for i in matrix:
            for j in i:
                ans.append(j)
        ans.sort()
        return ans[k-1]

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        # 核心思想
        # matrix是一个n*n的矩阵，每一行都是从小到大排列
        # 因此第一列上的数都是所在行上最小的数
        # 利用堆的特性，堆是一个二叉树，其中最小堆的每个父节点值都小于或等于其所有子节点的值。
        # 整个最小堆的最小元素总是位于二叉树的根节点。
        # python的heapq模块提供了对堆的支持。 heapq堆数据结构最重要的特征是heap[0]永远是最小的元素
        # heapq.heapify(list) ,将列表转换为堆
        # heapq.heappop(heap) ,删除并返回最小值，因为堆的特征是heap[0]永远是最小的元素，所以一般都是删除第一个元素。
        # heapq.heappush(heap, item)heap为定义堆，item增加的元素
        # 因此，先取出matrix中的第一列，并heappop删除最小的元素
        # 再添加一个删除元素所在行旁边的元素
        # 依次循环k-2次，第k-1次由return时返回（因为第k个元素的下标为k-1）
        # 参考图解：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/shi-yong-dui-heapde-si-lu-xiang-jie-ling-fu-python/

        n = len(matrix)  # 注：题目中这个矩阵是n*n的，所以长宽都是n

        pq = [(matrix[i][0], i, 0) for i in range(n)]  # 取出第一列候选人
        # matrix[i][0]是具体的值，i是所在行，0是所在列，方便每次右移添加下一个候选人
        
        heapq.heapify(pq)  # 变成一个heap

        for i in range(k - 1):  # 一共弹k-1次：这里k-2次，return的时候1次
            num, x, y = heapq.heappop(pq)  # 弹出候选人里最小一个
            if y != n - 1:  # 如果这一行还没被弹完
                # 加入这一行的下一个候选人
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))

        return heapq.heappop(pq)[0]
