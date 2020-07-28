# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        # 核心思想--递归
        # 本题与104相似，但需要注意，最小深度需要到叶子节点
        # 例如[1, 2]，返回值应该为2
        # 设置一个childDepth记录左子树和右子树的最小深度
        # 当左子树和右子树都有值时，则返回左子树和右子树中最小的一个
        # 当右子树或左子树中，某一个子树为空时，则返回有值得那棵子树，主要针对[1,2]这种情况
        # 当左右子树都为空时，返回0

        if not root : 
            return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        childDepth = min(leftDepth, rightDepth) if leftDepth and rightDepth else leftDepth or rightDepth
        return 1 + childDepth
