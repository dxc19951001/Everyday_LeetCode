# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 236.二叉树的最近公共祖先.py
    @date：2022/12/23 22:46
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 核心思想：后序遍历
        # 先找到p 和 q，然后在从p和q自身出发，再找到最近公共祖先
        # 递归参数：root p q
        # 递归终止条件1：当 当前节点 为空时返回空
        if not root:
            return root
        # 递归终止条件2：
        # 这里包含了两种情况
        # 情况1；p和q在左子树或右子树上，当 当前节点 等于p或q时，即找到了p或q，直接返回当前节点
        # 情况2：p为q的父节点，或q为p的父节点，这最近公共祖先即为q或p
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)  # 左
        right = self.lowestCommonAncestor(root.right, p, q)  # 右

        # 中
        # 当 当前节点 的左右子树都返回值时，说明p和q分别再左右子树上
        # 则当前节点为p和q的公共节点
        if left and right:
            return root
        # 当 当前节点 的左子树有返回值时，右子树没有返回值时，
        # 说明在左边找到p或q，或者是p和q的公共祖先
        # 向上回溯时，返回左子树的值
        if left:
            return left
        # 当 当前节点 的右子树有返回值时，左子树没有返回值时，则返回右子树的值
        # 说明在右边边找到p或q，或者是p和q的公共祖先
        # 向上回溯时，返回右子树的值
        if right:
            return right
