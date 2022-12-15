# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 03.成绩及格线.py
    @date：2022/12/15 15:20
"""
# 问题描述
# 10 个学生考完期末考试评卷完成后， A 老师需要划出及格线，要求如下：
# 及格线是 10 的倍数；
# 保证至少有 60%的学生及格；
# 如果所有的学生都高于 60 分，则及格线为 60 分
#
# 输入描述
# 输入 10 个整数，取值 0~100
#
# 输出描述
# 输出及格线， 10 的倍数
#
# 参考示例
# 示例 1
# 输入：90 78 91 99 60 86 92 98 99 100
#
# 输出：60
#
# 示例 2
# 输入：90 78 61 28 54 46 92 98 49 50
#
# 输出：50


def calc():
    nums_input = map(int, input().split())
    nums_input = sorted(nums_input, reverse=True)
    # 60% 的及格线
    # 将学生成绩安装降序排序，并取第6位学生成绩作为依据
    base = int(nums_input[5]/10) * 10
    if base > 60:
        print(60)
    else:
        print(base)


while True:
    try:
        calc()
    except:
        break
