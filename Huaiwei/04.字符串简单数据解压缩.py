# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 04.字符串简单数据解压缩.py
    @date：2022/12/15 15:39
"""
# 题目描述
# 将一段压缩后的字符串解压缩，并且排序输出
#
# 解压规则：
# 每个字符串后面跟随一个数字，表示这个字符串的重复次数。例如，“a5”解压缩的结果为“aaaaa”；“abc3”解压缩后的结果为“abcabcabc”。
#
# 排序规则
# 1、根据每个字符串的重复次数升序排序，然后输出结果。例如，“a3b2”，输出的结果为“bbaaa”。
# 2、如果字符重复次数一样，则根据 ASCII 编码顺序做升序排序，然后输出结果。例如，“b2a2”，输出的结果为“aabb”
#
# 输入描述
# 输入的原始字符串仅包含字母和数字
#
#
# 输出描述
#
# 输出的结果字符串仅包含字母
#
# 参考示例
# 输入：
#
# a11b2bac3bad3abcd2
#
#
# 输出：
#
# bb abcdabcd bacbacbac badbadbad aaaaaaaaaaa

import re


def calc():
    nums_input = input()
    # 使用正则表达式将字符串拆分
    # 例如a11b12，划分为["a", "11", "c", "12"]
    a = re.findall(r'\d+|\D+', nums_input)
    # 在上面的代码中，我们使用 re.findall 函数匹配字符串中的所有数字（即一个或多个连续的数字）和所有非数字（即一个或多个连续的非数字字符）
    # 我们使用 \d+ 匹配一个或多个数字，并使用 \D+ 匹配一个或多个非数字字符。
    # 最后，我们使用 | 符号将两个匹配模式组合起来，这意味着我们将匹配任意一个模式。

    chars = a[::2]
    nums = a[1::2]
    list1 = []

    # 将字符串和数字进行组合，变为[("a", 11), ("c", 12)]
    for i in range(len(chars)):
        list1.append((chars[i], int(nums[i])))

    # 按照ASCII码排序
    list1 = sorted(list1, key=lambda x: x[0])

    # 按照数字大小排序
    list1 = sorted(list1, key=lambda x: x[1])

    print("".join([key * count for key, count in list1]))


while True:
    try:
        calc()
    except:
        break


