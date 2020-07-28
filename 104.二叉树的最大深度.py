# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):

        # 核心思想--递归
        # 分别递归左子树和右子树，每次递归一层，
        # 返回左子树或右子树最大的深度，并加上本层的深度1
        # 递归出口：当递归到右子节点时，返回0

        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 
