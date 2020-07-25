from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        # 核心思想--二分查找
        # 题意理解
        # 将nums列表分成m个非空的连续子数组，求每种分发中每个子数字的和，并取出该种分法下最大的子数组和
        # 最终比较各种分法下的最大子数组和的最小值。
        # 示例nums = [7,2,5,10,8]，m = 2
        # 1.[7] [2,5,10,8] 最大子数组和：25
        # 2.[7，2] [5,10,8] 最大子数组和：23
        # 3.[7，2，5] [10,8] 最大子数组和：18
        # 4.[7，2，5，10] [8] 最大子数组和：24
        # 比较25 23 18 24，最终最小值为18

        # 对于一个nums列表
        #   当分成len(nums)等分时，则最终结果为列表中最大的那个数，即可能分成m等分的最小值
        #   当分成1等分时，则最终结果为列表中所有数的和，即可能分成m等分的最大值
        # 所以二分法中
        #   左边界为： left = max(nums)
        #   右边界为：right = sum(nums)
        # 当left < right，进行二分搜索，假设子数组各自和的最大值最小为mid = (left + right) // 2
        
        # 设定一个check函数，total=0记录nums中数据的和，cnt=1当前有几个子数组
        # 以mid为结果，当total + num > mid，
        #   则进入下一个新列表，此时新列表中total=num，列表个数cnt+=1
        # 当total + num >=mid
        #   则total +=num
        # 当循环完毕后，判断cnt是否cnt <= m
        # 若cnt <= m，说明若分成m段的结果可能<=此时的mid值
        #   因为在分成cnt都可以满足mid值，若nums分成更多的段即分成m段，则结果比必然小于等于mid
        #   则说明mid值偏大了，应该移动right，right=mid
        # 若cnt>m，说明分成m段的结果只可能比此时的mid值大
        #   因为在分成cnt满足mid值，但nums分成更小的段即分成m段，则结果比必然大于mid
        #   则说明此时的mid值偏小了，则应该移动left，left = mid + 1
        # 最终返回left

        def check(x: int) -> bool:
            # 设定check函数，对可能的值进行判断
            total, cnt = 0, 1  
            # total记录每个子数组的和；cnt记录当前分成了几段
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m

        left = max(nums)
        right = sum(nums)
        while left < right:
            # 二分搜索模板
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left