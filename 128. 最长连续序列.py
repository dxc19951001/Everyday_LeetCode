class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 核心思想：
        # 1.判断是否空列表，空列表直接返回
        # 2.使用set去重
        # 3.用冒泡排序进行排序，最优时间复杂度为O(n)
        # 4.对排序后的列表进行比较，前一个数+1是否等于现在的数，如果存在，则序列长度+1
        # 5.直至循环完成，得到最大的序列长度

        if nums:
            nums = list(set(nums))
            for j in range(len(nums)-1,0,-1):
            # j表示每次遍历需要比较的次数，是逐渐减小的
                for i in range(j):
                    if nums[i] > nums[i+1]:
                        nums[i], nums[i+1] = nums[i+1], nums[i]
            
            cur=1
            MAX = 1
            for i in range(len(nums)):
                if (nums[i - 1] + 1 == nums[i]):
                    cur +=1
                else:
                    MAX = max(MAX, cur)
                    cur = 1
            return max(MAX, cur)
        
        else:
            return 0

        

    def longestConsecutive_Hash(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 核心思路
        # 1.利用set去重
        # 2.对于一个数x，若在set中无x-1，则x为连续序列的开始
        # 3.判断x+1、x+2...是否存在于set中，若存在则连续序列长度+1
        # 4.直至循环完成，得到最大的训练长度


        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


s = Solution()
# a = s.longestConsecutive([100, 4, 200, 1, 3, 2])
a = s.longestConsecutive([0, 1])

print(a)

b = s.longestConsecutive_Hash([100, 4, 200, 1, 3, 2])
print(b)


