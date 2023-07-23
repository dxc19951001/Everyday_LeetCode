# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 222.完全二叉树的节点个数.py
    @date：2022/12/23 12:09
"""


class Solution(object):

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 核心思想：BFS，层序遍历每一个节点，最后统计节点数

        if not root:
            return 0

        queue = [root]
        result = []

        while len(queue):
            node = queue.pop(0)
            result.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return len(result)

    def countNodes2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 核心思想：后序遍历
        # 左右字节的的个数返回到中间节点

        if not root:
            return 0
        left_count = self.countNodes(root.left)  # 左
        right_count = self.countNodes(root.right)  # 右
        return 1 + left_count + right_count  # 中
