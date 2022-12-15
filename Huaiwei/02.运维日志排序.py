# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 02.运维日志排序.py
    @date：2022/12/15 11:12
"""

# 题目描述
# 运维工程师采集到某产品线网运行一天产生的日志n条，现需根据日志时间先后顺序对日志进行排序，日志时间格式为H:M:S.N。
# H表示小时(0~23)
# M表示分钟(0~59)
# S表示秒(0~59)
# N表示毫秒(0~999)
#
# 时间可能并没有补全，也就是说，01:01:01.001也可能表示为1:1:1.1。
#
# 输入描述：
# 第一行输入一个整数n表示日志条数，1<=n<=100000，接下来n行输入n个时间。
#
# 输出描述：
# 按时间升序排序之后的时间，如果有两个时间表示的时间相同，则保持输入顺序。

# 测试用例
# 示例：
# 1.输入：
# 2
# 01:41:8.9
# 1:1:09.211
#
# 输出：
# 1:1:09.211
# 01:41:8.9
#
# 2.输入：
# 3
# 23:41:08.023
# 1:1:09.211
# 08:01:22.0
#
# 输出：
# 1:1:09.211
# 08:01:22.0
# 23:41:08.023
#
# 3.输入：
# 2
# 22:41:08.023
# 22:41:08.23
#
# 输出：
# 22:41:08.023
# 22:41:08.23


def calc():
    # 输入一
    num = int(input())
    list1 = []
    for i in range(num):
        # 输入二
        input_str = input()
        # 小时，分钟截断，秒和毫秒做特殊处理
        h, m, last = input_str.split(":")

        if "." in last:
            # 根据 . 将秒 和 毫秒截断
            last_arr = last.split(".")
            len1 = list(last_arr)
            if len(len1) == 2:
                s, n = last_arr
                list1.append([int(h), int(m), int(s), int(n), str(input_str)])
    # 根据列表中的数据大小排序
    list1.sort()

    for j in list1:
        print(j[-1])


while True:
    try:
        calc()
    except:
        break
