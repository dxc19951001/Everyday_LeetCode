# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 22.括号生成.py
    @date：2023/1/17 0:29
"""

# 参考：https://leetcode.cn/problems/generate-parentheses/solution/sui-ran-bu-shi-zui-xiu-de-dan-zhi-shao-n-0yt3/

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 回溯算法
        # 回溯参数：path回溯路径，left左括号数，right右括号数
        # 终止条件：
        #   1.len(path) == 2 * n，表明括号对已经找完了
        #   2.left > n，因为左括号和右括号，都是一人一半的，所以不会超过n
        #   3.right > left，因为一人一半，所以右括号数不会超过括号数
        # 单层回溯：
        #   先加入"("，左括号数加1，继续递归，直至递归终止条件，再加入")"
        # 因为path是字符串，返回到上一层递归时，去掉了这层递归加上的括号，隐含了回溯

        res = []
        path = ""
        left = right = 0

        def backtrack(path, left, right):
            if left > n or right > left:
                return

            if len(path) == 2 * n:
                res.append(path)
                return

            backtrack(path + "(", left + 1, right)
            backtrack(path + ")", left, right + 1)

        backtrack(path, left, right)

        return res

s = Solution()
s.generateParenthesis(2)