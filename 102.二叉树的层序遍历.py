# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 102.二叉树的层序遍历.py
    @date：2022/12/20 16:10
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 使用BFS思路求解
        # 使用队列，将节点加入后，先进先出

        if not root:
            return root

        queue = []  # 设定BFS队列
        result = []  # 返回的结果列表
        queue.append(root)  # 队列中加入头节点

        while len(queue) > 0:
            # 循环每一层的节点值
            result.append([node.val for node in queue])
            # 临时存放下一层的所有节点
            tmp = []
            # 循环当前层的所有节点
            for node in queue:
                # 如果左子节点存在，入队列
                if node.left:
                    tmp.append(node.left)
                # 如果右子节点存在，入队列
                if node.right:
                    tmp.append(node.right)
            # 当前节点全部循环完成后，则进入下一层
            queue = tmp
        return result