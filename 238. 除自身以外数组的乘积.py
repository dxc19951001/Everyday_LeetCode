class Solution(object):
    def productExceptSelf_0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 核心思想：
        # 用两层for循环可以轻松解决，时间复杂度为n^2,不符合题目要求
        # 核心：利用列表切片，每次循环将不参与计算的数组剔除
        
        output= [0] * len(nums)
        for i in range(len(nums)):
            j = 1
            news = nums[:i] + nums[i+1 :]
            for k in news:
                j *= k
            output[i] = j
        return output


    
    def productExceptSelf_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 核心思想：
        # 分别定义i左边数组、右边数组、答案数组
        # 分别计算i的左边数组和右边数组中每个的乘积，再将对应元素相乘即可得到答案

        length = len(nums)
        
        # L 和 R 分别表示左右两侧的乘积列表
        L, R, answer = [0]*length, [0]*length, [0]*length
        
        # L[i] 为索引 i 左侧所有元素的乘积
        # 对于索引为 '0' 的元素，因为左侧没有元素，所以 L[0] = 1
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        
        # R[i] 为索引 i 右侧所有元素的乘积
        # 对于索引为 'length-1' 的元素，因为右侧没有元素，所以 R[length-1] = 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            # 相当于从(length-2)一直到0
            R[i] = nums[i + 1] * R[i + 1]

        # 对于索引 i，除 nums[i] 之外其余各元素的乘积就是左侧所有元素的乘积乘以右侧所有元素的乘积
        for i in range(length):
            answer[i] = L[i] * R[i]
        
        return answer
    
    
    def productExceptSelf_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 核心思想：
        # 节约空间aanswer和左侧所有元素乘积公用一块空间
        # answer[i] 表示索引 i 左侧所有元素的乘积
        # 因为索引为 '0' 的元素左侧没有元素， 所以 answer[0] = 1


        length = len(nums)
        answer = [0]*length
        
        
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R 为右侧所有元素的乘积
        # 刚开始右边没有元素，所以 R = 1
        R = 1
        for i in reversed(range(length)):
            # 对于索引 i，左边的乘积为 answer[i]，右边的乘积为 R
            answer[i] = answer[i] * R
            # R 需要包含右边所有的乘积，所以计算下一个结果时需要将当前值乘到 R 上
            R *= nums[i]
        
        return answer

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 用两个常量分别来计算左边数组和右边数组

        left = 1
        right = 1
        result = [1] * len(nums)
        # 算出左边列表
        for i in range(len(nums)):
            result[i] *= left 
            left *= nums[i]
        
        # 算出右边列表
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result




nums = [1,2,3,4]

s = Solution()
a = s.productExceptSelf(nums)
print(a)