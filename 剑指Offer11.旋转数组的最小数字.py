class Solution:
    def minArray(self, numbers: [int]) -> int:
        
        # 核心思想
        # 二分查找
        # 例如：numbers = [3, 4, 5, 6, 1, 2, 3]
        # 左边为[3, 4, 5, 6],右边为[1, 2, 3]
        # 性质左边数组中的每一个数大于等于右边数组中的每一个数
        # i，j分别在数组numbers的两端，m = (i + j) // 2，设最小的数为x，其为旋转点
        # 若numbers[m] > numbers[j]，则m在左边数组中，则x在[m+1, j]中，令i=m+1
        # 若numbers[m] < numbers[j]，则m在右边数组中，则x在[i, m]中，令j=m
        # 特殊情况numbers[m] == numbers[j],例如：[1,1,1,0,1],m=2,j=4,numbers[m] == numbers[j]
        # 此时 j -= 1，缩小范围
        # 当i=j时，返回numbers[i]

        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]: i = m + 1
            elif numbers[m] < numbers[j]: j = m
            else: j -= 1
        return numbers[i]
