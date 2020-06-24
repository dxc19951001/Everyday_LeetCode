class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 核心思想
        # 排序+双指针
        # 先对列表排序，然后采用双指针方法
        # 每次先固定一个值nums[i]，
        # 设定数值小的指针为nums[i+1]，数值大的指针为nums[len(nums) - 1 ]
        # 每次计算sum = nums[i] + nums[i+1] + nums[len(nums) - 1 ]
        # 设diffnum用来记录与sum与target差的绝对值，设ans记录此次的sum
        # 若计算的出比上一次的小，则更新diffsum 和 ans
        # diffnum为int类型的最大值

        n = len(nums)
        nums.sort()
        import sys
        diffnum = sys.maxsize  # 设定diffnum为int类型的最大值
        ans = 0

        for i in range(n-2):
            k, j = i + 1, len(nums) - 1  # 设定双指针
                       
            while k < j:
                # 若小的指针移动至大指针右侧则结束循环
                sum = nums[i] + nums[k] + nums[j]
                tmp = abs(sum - target)
                if tmp < diffnum:
                    # 若此处差值比上次小，则跟新diffnum 和 sum
                    diffnum  = tmp
                    ans = sum
                if sum == target:
                    # 若sum 正好等于target返回target
                    return target
                elif sum < target:
                    # 若sum小于target，则移动数值小的指针向右，增大sum
                    k += 1
                else:
                    # 若sum大于target，则移动数值大的指针向左，减小sum
                    j -= 1
        return ans



nums = [-1,2,1,-4]
x = 1

s = Solution()
a = s.threeSumClosest(nums, x)
print(a)