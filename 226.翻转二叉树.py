# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        # 核心思想--递归
        # 递归将左子树和右子树进行交换

        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root