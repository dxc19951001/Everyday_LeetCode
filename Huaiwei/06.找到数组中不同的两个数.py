# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 06.找到数组中不同的两个数.py
    @date：2022/12/15 18:57
"""

# 题目描述
#
# 在一个长度为 n 的数组 nums 里的数组中，数字两两相同，有两个不同，找出数组中不同的这两个数。
#
# 参考示例
# 示例 1
# 输入：2 3 1 5 2 5 3 7
# 输出：1 7


def calc():
    nums_input = list(map(int, input().split()))
    ret = []
    for c in nums_input:
        # 统计列表中的元素是否只有1个
        if nums_input.count(c) == 1:
            ret.append(str(c))
    print(" ".join(ret))


while True:
    try:
        calc()
    except:
        break
