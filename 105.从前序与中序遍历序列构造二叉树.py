# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 105.从前序与中序遍历序列构造二叉树.py
    @date：2022/12/20 19:15
"""

# Definition for a binary tree node.

# todo
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        n = inorder.index(root.val)
        preorder.pop(0)
        root.left = self.buildTree(preorder[:n], inorder[:n])
        root.right = self.buildTree(preorder[n:], inorder[n + 1:])
        return root


l1 = [3,9,20,15,7]
l2 = [9,3,15,20,7]

s = Solution()

s.buildTree(l1, l2)