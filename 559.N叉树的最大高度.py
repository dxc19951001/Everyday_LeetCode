# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 559.N叉树的最大高度.py
    @date：2022/12/23 0:11
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # 核心思想：后序遍历
        # 遍历每一个节点的最大深度

        if not root:
            return 0

        depth = 0
        for i in range(len(root.children)):
            depth = max(depth, self.maxDepth(root.children[i]))
        return depth + 1