class Solution(object):
    def firstMissingPositive1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 核心思想
        # 找出nums中所有大于等于0的数，构建新列表nums
        # for循环从1到len(nums)+1，（加1是因为，for循环左闭右开，加1才能取到len(nums)）
        # 依次判断1，2，3....是否在lists中
        # 若有不存在，则返回不存在的正整数

        # 特殊情况
        # 1.nums为空，返回1
        # 2.nums从1到len(nums)，都存在，则返回max(nums)+1

        # 缺点，简单思路不符合要求（但网站对程序没有限制，可以通过）
        # 题目要求：你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
        # in操作在list中时间复杂度为O(n),则总体复杂度为O(n^2)
        # in操作在dict/set中时间复杂度为O(1)，但空间复杂度不为常数，也不符合要求
   
        nums = [i for i in nums if i >=0]
        if not nums:
            # 特殊情况1
            return 1
        for j in range(1, len(nums) + 1):
            # 依次判断1，2，3....是否在lists中
            if j not in nums:
                return j
        return max(nums)+1  # 特殊情况3



    from typing import List
    def firstMissingPositive(self, nums: List[int]) -> int:

        # 核心思想
        # 将数组视为哈希表
        # 由于题目要求我们「只能使用常数级别的空间」，
        # N为nums长度
        # 而要找的数一定在 [1, N + 1] 左闭右闭（这里 N 是数组的长度）这个区间里。
        # 因此，我们可以就把原始的数组当做哈希表来使用。事实上，哈希表其实本身也是一个数组；
        
        # 我们要找的数就在 [1, N + 1] 里，最后 N + 1 这个元素我们不用找。因为在前面的 N 个元素都找不到的情况下，我们才返回 N + 1；
        # 那么，我们可以采取这样的思路：就把 1这个数放到下标为 0的位置， 2这个数放到下标为 1的位置，
        # 例如[1,2,3],则对应的下标为[0,1,2]
        # 按照这种思路整理一遍数组。然后我们再遍历一次数组，第 1个遇到的它的值不等于下标的那个数，就是我们要找的缺失的第一个正数。
        
        # 这个思想就相当于我们自己编写哈希函数，这个哈希函数的规则特别简单，那就是数值为 x 的数映射到下标为 x - 1 的位置。

        # 编码实现
        # 列表长度：size = len(nums)
        # 循环遍历列表nums，当1 <= nums[i] <= size并且nums[i] != nums[nums[i] - 1]，
        # 交换nums[i]和nums[nums[i] - 1]的位置,使得nums[i]回到正确的位置上
        # 1 <= nums[i] <= size：确保在正确位置的数值范围在[1,size]，对于超过范围的正整数不关心其位置正确与否
        # nums[i] != nums[nums[i] - 1]：因为我们设定的哈希表规则：数值为 x 的数映射到下标为 x - 1 的位置
        # 如果数字在正确的位置上，nums[i]为数值x，nums[i]-1表示数值应该在x-1位置的下标，
        # 若数值所在位置正确，则nums[i] == nums[nums[i] - 1]
        #   例如一个不正确的情况，nums=[2, 1]，
        #   nums[0] = 2, nums[0]-1=1，而此时nums[nums[0]-1]=1,nums[0] !=nums[nums[0]-1]
        #   说明nums[0]没有在正确的位置上，交换交换nums[0]和nums[nums[0] - 1]，即交换nums[0]和nums[1]
        #   此时nums为[1,2],每个数字都在了正确的位置上了
        
        # 对列表处理完毕，使得每一个正整数都在其正确的位置上后
        # 循环列表，当出现i + 1 != nums[i]时，即表示nums[i]处缺失正整数，返回i+1
        # 若循环完成没有缺失，则说明列表缺失最后一位，返回size + 1

        size = len(nums)
        for i in range(size):
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                # 在范围内位置不正确的数字交换位置
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

                # 若这样写会报错，建议此处封装成单独的函数，避免出错。
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
        
        for i in range(size):
            # 循环排序后的nums，找出第一个位置不正确的数值
            if i + 1 != nums[i]:
                return i + 1
        return size + 1  # 若循环完成未找到，则说明列表缺失最后一位，返回size + 1



    
s = Solution()
nums = [3,4,-1,1]
a = s.firstMissingPositive(nums)

print(a)