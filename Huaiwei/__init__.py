# def search(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#
#     # 设置一个左闭右闭的区间
#     left = 0
#     right = len(nums) - 1
#
#     # 因为是左闭右闭的区间left可以等于right，所以要<=
#     while left <= right:
#         # 找到这个区间的中间索引
#         mid = (left + right) // 2
#         print(mid)
#         # left+(right-left)/2   用来防止溢出
#         # 如果中间索引位置的值大于target
#         if nums[mid] >= target:
#             # 则右边指针指向mid-1位置
#             # 因为mid的位置已经判断过了
#             right = mid - 1
#         # 最后返回mid，即target的值
#         else:
#             left = mid + 1
#     # 如果没有找到返回-1
#     return left
#F
# a = [1,2,3,3,3,4,5]
# target = 3
#
# x = search(a, target)
# print(x)

# print(1//2)


a = {"a":[1,2], "b":2}

print(list(a.values()))