# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        # 核心思想--后序遍历
        # 本题与104相似，但需要注意，最小深度需要到叶子节点

        if not root:
            return 0

        left_depth = self.minDepth(root.left)  # 左
        right_depth = self.minDepth(root.right)  # 右

        # 中
        # 当节点没有右子树时应计算左子树的最小深度，当节点没有左子树时应计算左右树的最小深度
        # 因为题目要求的时叶子节点到根节点的最小深度
        if root.left is not None and root.right is None:
            return 1 + left_depth
        if root.right is not None and root.left is None:
            return 1 + right_depth
        # 当运行到叶子节点时，向上返回
        return 1 + min(left_depth, right_depth)
