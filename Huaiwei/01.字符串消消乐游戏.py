# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 01.字符串消消乐游戏.py
    @date：2022/12/15 11:12
"""

# 题目描述 https://blog.csdn.net/forest_long/article/details/125803208
# 输入一个只包含英文字母的字符串，字符串中的两个字母如果相邻且相同，就可以消除。
# 在字符串上反复执行消除的动作，直到无法继续消除为止，此时游戏结束。
# 输出最终消除完后留下的字符串。


while True:
    try:
        a = input()
        stack = []
        for i in a:
            # 如果列表为空则加入新的字符串
            if not stack:
                stack.append(i)
            else:
                # 如果新加入的字符与最后一个相等，则剔除最后一个字符
                if i == stack[-1]:
                    stack.pop()
                # 如果新的字符，则加入列表
                else:
                    stack.append(i)

        print("".join(stack))
    except:
        break



