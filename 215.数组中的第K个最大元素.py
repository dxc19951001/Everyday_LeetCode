class Solution(object):
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # 偷懒写法
        # 利用sort函数对nums进行降序排列
        # 直接返回第k个数

        nums.sort(reverse=True)
        return nums[k-1]   
   