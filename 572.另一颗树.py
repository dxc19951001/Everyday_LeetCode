# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 572.另一颗树.py
    @date：2022/12/22 23:43
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # 核心思想：后序遍历，通过左子树和右子树的结果返回到中间节点，判断结果
    # 判断两个树是否相等的三个条件是与的关系，即：
    #
    # 当前两个树的根节点值相等；
    # 并且，s 的左子树和 t 的左子树相等；
    # 并且，s 的右子树和 t 的右子树相等。
    # 而判断 t 是否为 s 的子树的三个条件是或的关系，即：
    #
    # 当前两棵树相等；
    # 或者，t 是 s 的左子树；
    # 或者，t 是 s 的右子树。

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # 判断是否为子树的方法
        # 参数为树s和子树t

        # 迭代终止条件为
        # 树s的节点为空，并且子树t为空，则返回True
        # 树s的节点为空，或者子树t为空，则返回False
        #   这对应2种情况：1.s为空，t不为空；2.s不为空，t为空
        # 如果s和t都有值则继续向下递归执行
        if not s and not t:
            return True
        if not s or not t:
            return False

        same_tree = self.isSameTree(s, t)
        left_same_tree = self.isSubtree(s.left, t)
        right_same_tree = self.isSubtree(s.right, t)
        return same_tree or left_same_tree or right_same_tree

    # 封装一个判断树是否相等的方法，参考第100题
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False

        bool_left = self.isSameTree(s.left, t.left)
        bool_right = self.isSameTree(s.right, t.right)
        # 返回到中间节点是左节点和右节点的布尔值
        return bool_left and bool_right