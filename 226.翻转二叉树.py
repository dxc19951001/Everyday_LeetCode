# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    class Solution(object):
        def invertTree(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            # 按照前序遍历的思路
            # 参数为root，返回值也为root
            # 递归终止条件为root为空
            # 在前序遍历的中间层，交换左右子节点

            if not root:
                return root

            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
