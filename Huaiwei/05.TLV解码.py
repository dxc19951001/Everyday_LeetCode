# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 05.TLV解码.py
    @date：2022/12/15 18:33
"""
# 题目描述
#
# TLV编码是按[Tag Length Value]格式进行编码的，一段码流中的信元用Tag标识，Tag在码流中唯一不重复，Length表示信元Value的长度，Value表示信元的值。
#
# 码流以某信元的Tag开头，Tag固定占一个字节，Length固定占两个字节，字节序为小端序。
#
# 现给定TLV格式编码的码流，以及需要解码的信元Tag，请输出该信元的Value。
#
# 输入码流的16机制字符中，不包括小写字母，且要求输出的16进制字符串中也不要包含小写字母；码流字符串的最大长度不超过50000个字节。
#
#
# 输入描述
# 输入的第一行为一个字符串，表示待解码信元的Tag；
#
# 输入的第二行为一个字符串，表示待解码的16进制码流，字节之间用空格分隔。
#
# 输出描述
# 输出一个字符串，表示待解码信元以16进制表示的Value。
#
# 参考示例
#
# 输入
#
# 31
# 32 01 00 AE 90 02 00 01 02 30 03 00 AB 32 31 31 02 00 32 33 33 01 00 CC
#
#
# 输出：
#
# 32 33
#
# 说明：
# 需要解析的信源的tag是31
# 从码流的起始处开始匹配，tag为32的信元长度为1(01 00,小端序表示为1)
# 第二个信元的tag为90 其长度为2
# 第三个信元的tag为30 其长度为3
# 第四个信元的tag为31 其长度为2(02 00)
# 所以返回长度后面的两个字节即可 为 32 33


def calc():
    nums_input = input()
    dct = {}
    nums = input().split()
    key = None
    lens = None
    while nums:
        if key:
            if lens:
                # 根据 整型信元长度 截取 Value
                dct[key] = nums[0:int(lens)]
                nums = nums[int(lens):]
                key = None
                lens = None
            else:
                # 获取两字节信元长度
                lens = int("".join(nums[0:2][::-1]))
                nums = nums[2:]
        else:
            # 获取信元的nums_input
            key = nums[0]
            nums = nums[1:]
    print(" ".join(dct[nums_input]))


while True:
    try:
        calc()
    except:
        break