# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 08.特殊计算.py
    @date：2022/12/15 22:30
"""
# 题目描述
#
# 特殊符号代替普通的计算方式比如 x#y = 2*x+y，x$y = x+3y， #优先级高于$。
# 比如输入 5#2$6 输出结果就是 30，因为先算 5#2 = 12，再算 12$6=30
#
# 参考示例
#
# 输入：5#2$6
# 输出：30


def calc():
    num_input = input()
    stack = []
    i = 0
    j = 1

    # 将数字和计算符合整合
    # 例如123#4356$789 变为[123, "#", 456, "$", 789]
    while j < len(num_input):
        if num_input[j] == "#":
            stack.append(int("".join(num_input[i:j])))
            stack.append(num_input[j])
            i = j + 1
        elif num_input[j] == "$":
            stack.append(int("".join(num_input[i:j])))
            stack.append(num_input[j])
            i = j + 1
        j += 1
    else:
        stack.append(int("".join(num_input[i:j])))

    # 先进行# 运算
    #  # 前1个数子变为2倍
    while "#" in stack:
        i = stack.index("#")
        stack[i - 1] = 2 * stack[i - 1]
        stack.pop(i)

    # 在进行$运算
    # $后一个数字变为3倍
    while "$" in stack:
        i = stack.index("$")
        stack[i + 1] = 3 * stack[i + 1]
        stack.pop(i)
    # 最终所有数字求和
    print(sum(stack))



while True:
    try:
        calc()
    except:
        break