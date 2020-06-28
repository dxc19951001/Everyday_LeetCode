class Solution(object):
    def minSubArrayLen1(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        # 核心思想
        # 循环nums，找到nums[i]的前i-k个数，使其累加和大于等于s
        # 设定初始变量 ans 连续正整数的个数，ans最大值为nums中全部数相加才大于等于s，所以为len(nums)
        # 若有符合条件的连续 n 个正整数, ans=i-k+1，记录连续正整数的个数
        # 若下次有符合条件的连续正整数的个数比之前的ans少，则更新ans

        # 考虑特殊情况
        # 没有nums或者sum(nums) < s，返回0

        if not nums or sum(nums) < s:
            return 0

        ans = len(nums)
        for i in range(len(nums)):
            sums = 0
            for k in range(i, -1, -1):
                sums += nums[k]
                if sums >= s:
                    ans = min(ans, i-k+1)
                    break
        return ans

    from typing import List
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        # 核心思想
        # 双指针
        # left和right分别指向nums的第一位。
        # 设定初始变量 res 连续正整数的个数，res最大值为nums中全部数相加才大于等于s，所以为len(nums)
        # 设定连续正整数相加的和为sum_lr

        # 在右指针right小于 len(nums) 长度的情况下，进行循环
        #   当sum_lr小与s，且 right<len(nums),保证right小于len(nums)，则右指针right右移，增大sum_lr
        #   当sum_lr大于s，且right>left,保证左指针不会跑到右指针的右边，则左指针left右移，减小sum_lr
        #       此时right-left，当res比之前小时，更新res

        # 特殊情况：sum(nums) < s，返回0
        
        if s > sum(nums):
            return 0
        left, right, res, sum_lr = 0, 0, len(nums), 0  # 双指针都从第一位出发
        while right < len(nums):
            while sum_lr < s and right < len(nums):  # sum_lr小与s则右指针右移
                sum_lr += nums[right]
                right += 1
            while sum_lr >= s and right > left:  # sum_lr大于s则左指针右移
                res = min(res, right-left)
                sum_lr -= nums[left]
                left += 1
        return res


s = Solution()
x = 11
nums = [1, 11, 3]
a = s.minSubArrayLen(x, nums)
print(a)
