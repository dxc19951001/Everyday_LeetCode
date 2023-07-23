# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 101.对称二叉树.py
    @date：2022/12/22 18:50
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # 核心思想：后序遍历

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        # 首先排除空节点的情况
        # 左子树节点为空，右子树节点不为空，则两边不想等，不能翻转，返回False
        if left is None and right is not None:
            return False
        # 左子树节点不为空，右子树节点为空，则两边不相等，不能翻转，返回False
        elif left is not None and right is None:
            return False
        # 左子树节点为空，右子树节点为空，则两边相等，返回True
        elif left is None and right is None:
            return True
        # 排除了空节点，再排除数值不相同的情况
        elif left.val != right.val:
            return False

        # 此时就是：左右节点都不为空，且数值相同的情况
        # 此时才做递归，做下一层的判断
        # 比较左节点的左节点和右节点的右节点
        outside = self.compare(left.left, right.right)  # 左子树：左、 右子树：右
        # 比较左节点的右节点和右节点的左节点
        inside = self.compare(left.right, right.left)  # 左子树：右、 右子树：左
        # 只有子节点的里侧和外侧都相等，则返回True
        isSame = outside and inside  # 左子树：中、 右子树：中 （逻辑处理）
        return isSame