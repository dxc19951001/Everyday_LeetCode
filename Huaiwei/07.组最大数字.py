# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 07.组最大数字.py
    @date：2022/12/15 19:05
"""
# 题目描述
#
# 给出几组字符串的数字，需要获得组成的最大数字。
# 比如输入 123， 546， 8， 32，输出 854632123
#
#
# 输入格式
#
# 有多组测试样例，每行包含N个数(每个数不超过1000，空格分开)。
#
#
# 输出格式
#
# 每组数据输出一个表示最大的整数。
#
# 参考示例
#
# 示例 1
# 输入：12 123
# 输出：12312
#
# 示例 2
# 输入：123 546 8 32
# 输出：854632123


def calc():
    nums_input = input().split()
    print(nums_input)
    # 降序排序，先比较最高位，如果相同再比较第二高位，依次类推
    nums_input = sorted(nums_input, reverse=True)
    print(nums_input)
    print(int("".join(nums_input)))

    # 存在问题999 9998 类似组合时会出问题


def calc1():
    global nums_input, base
    nums_input = input().split()
    base = list(range(len(nums_input)))

    def dfs(val):
        if len(val) == len(nums_input):
            return int("".join([nums_input[v] for v in val]))

        for i in base:
            if i not in val:
                return dfs(val + [i])

    dp = []
    for i in base:
        dp.append(dfs([i]))
    print(max(dp))

    # 1 999 9998 组合时会出问题


while True:
    try:
        calc()
    except:
        break
