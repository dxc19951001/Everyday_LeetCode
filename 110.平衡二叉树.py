# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 110.平衡二叉树.py
    @date：2022/12/23 13:01
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # 核心思想:后序遍历
    # 通过后序遍历求出每个节点的左子树和右子树的最大高度，比较差值是否小于等于1
    # 递归参数：root
    # 递归终止条件：root为空
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        # 单层递归
        left_bool = self.isBalanced(root.left)  # 左
        right_bool = self.isBalanced(root.right)  # 右
        mid_bool = abs(self.calHigh(root.left) - self.calHigh(root.right)) <= 1  # 中，中间的节点比较左右子树的差值是否小于等于1

        return left_bool and right_bool and mid_bool  # 如果上述条件都满足则返回True

    def calHigh(self, root):
        # 计算左右子树的最大高度
        if not root:
            return 0
        left_depth = self.calHigh(root.left)
        right_depth = self.calHigh(root.right)
        return max(left_depth, right_depth) + 1