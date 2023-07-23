# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 404.左叶子之和.py
    @date：2022/12/23 19:08
"""

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 核心思想：后序遍历，计算左子树和右子树的左叶子节点值的和
        # 递归参数：root
        # 递归终止条件：root为空

        if not root:
            return 0
        # 单层递归
        # 1.计算左子树的左叶子节点的值的和
        left_left_leaves_sum = self.sumOfLeftLeaves(root.left)  # 左
        # 2.计算右子树的左叶子节点的值的和
        right_left_leaves_sum = self.sumOfLeftLeaves(root.right)  # 右
        # 3.如果当前节点是一个左叶子节点，则返回当前节点的值加上其他左叶子节点的值 的和
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + left_left_leaves_sum + right_left_leaves_sum  # 中
        # 4.如果当前节点不是一个左叶子节点，则返回其他左叶子节点的值 的和
        return left_left_leaves_sum + right_left_leaves_sum
