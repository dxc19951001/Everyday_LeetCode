class Solution(object):
    def threeSum_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 核心思想：
        # 循环暴力求解
        # 对列表排序后，从后向前循环
        # 第一层循环找到i，范围是:[2,n-1]
        # 第二层循环找到k，范围是:[1,i-1]
        # 第三层循环找到k，范围是:[0,k-1]
        # 这样可以循环遍历出所有解
        # 求解后可能出现重复的情况，再进行去重
        # 时间复杂度O(n**3),数据量大了极其慢
        # 只需要常数变量，空间复杂度为O(1)

        nums.sort()
        n = len(nums)
        tmp = list()
        ans = list()

        for i in range(n-1, 1, -1):
            a = nums[i]
            for k in range(i-1, 0, -1):
                b = nums[k]
                for j in range(k-1, -1, -1):
                    c = nums[j]
                    if a + b + c == 0:
                        tmp.append([a, b, c])
        # 去重
        for li in tmp:
            if li not in ans:
                ans.append(li)
        return ans

    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 核心思想:
        # 双指针解法
        # 对列表从小到大排序
        # 固定3个指针中最左（最小）数字的指针 k
        # 双指针 i，j分设在数组索引[k+1, len(nums)-1]两端
        # 每次循环，固定并记录k，双指针i. j交替向中间移动
        # 找出所有满足 nums[k] + nums[i] + nums[j] == 0 的 i,j 组合
        
        # 由于三个数相加等于0，必然最小的数k要小于0
        # 所以当nums[k]大于等于0时，不可能存在解，直接break结束
        # 当 k > 0，第一个元素之后，当nums[k] == nums[k - 1]时，则跳过此元素nums[k]：
        # 因为已经将 nums[k]和nums[k - 1]值相同， nums[k - 1]所有组合和nums[k]的组合重复了

        # i，j 分设在数组索引[k+1, len(nums)-1]两端，
        # 当i < j时循环计算s = nums[k] + nums[i] + nums[j]，并按照以下规则执行双指针移动：
        #     当s < 0时，i += 1并跳过所有重复的nums[i]，i向中间移动；
        #     当s > 0时，j -= 1并跳过所有重复的nums[j]，j向中间移动；
        #     当s == 0时，记录组合[k, i, j]至res，执行i += 1和j -= 1并跳过所有重复的nums[i]和nums[j]，防止记录到重复组合。
        # 移动至i>=j时，本次固定的k寻找满足条件的i, j 已搜索完，进行下一轮循环，固定新的k
            
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                # 判断最小额k值是否大于0
                # 大于0，三个数相加不可能等于0，直接跳出循环
                break  
            if k > 0 and nums[k] == nums[k - 1]:
                # 当k大于0时，判断nums[k]值是否重复，若重复直接进入下一轮循环
                continue 
            i, j = k + 1, len(nums) - 1  # 设定双指针
            while i < j: 
                # 若i<j进行移动指针
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    # s值小于0，则移动i，使得s变大
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        # 跳过重复的i
                        i += 1
                elif s > 0:
                    # s值大于0，则移动j，使得s变小
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        # 跳过重复的j
                        j -= 1
                else:
                    # s = 0，记录下满足要求的数，并继续移动i，j
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        # 跳过重复的i
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        # 跳过重复的j
                        j -= 1
        return res

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if nums[i] > 0:
                return ans
            if i >= 1 and nums[i] == nums[i - 1]:
                # 对数字a去重
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        # 对数字b去重
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        # 对数字c去重
                        right -= 1
                    left += 1
                    right -= 1

        return ans


s = Solution()
nums = [-1, 0, 1, 2, -1, -4]

print(s.threeSum(nums))
